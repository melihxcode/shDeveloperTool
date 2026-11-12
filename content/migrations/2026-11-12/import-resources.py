"""Import data only; never extract/run a program or execute a SQL script."""
import hashlib
import io
import json
import os
import re
import subprocess
import tempfile
import urllib.request
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root/'resource-manifest.json').read_text())
repo = os.environ['GITHUB_REPOSITORY']
assert repo == 'melihxcode/shDeveloperTool'
assert manifest['sourceRepository'] == 'melihxcode/shDeveloperPack'
commit = manifest['sourceCommit']
assert re.fullmatch('[0-9a-f]{40}',commit)
tag = manifest['tag']
assert re.fullmatch('resources-[0-9-]+',tag)
def gh(*args):
    return subprocess.check_output(['gh',*args],text=True)
with tempfile.TemporaryDirectory() as temp:
    work = Path(temp)
    url = f'https://codeload.github.com/{manifest["sourceRepository"]}/zip/{commit}'
    with urllib.request.urlopen(url,timeout=180) as response:
        snapshot = response.read(150*1024*1024)
        assert not response.read(1), 'Unexpected snapshot size'
    source = zipfile.ZipFile(io.BytesIO(snapshot))
    prefix = source.namelist()[0]
    paths = []
    for item in manifest['assets']:
        name = item['fileName']
        assert re.fullmatch('[a-z0-9.-]+',name) and '/' not in name
        if 'sourcePath' in item:
            data = source.read(prefix+item['sourcePath'])
        else:
            stream = io.BytesIO()
            with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_STORED) as bundle:
                for path in item['bundleSources']:
                    info = zipfile.ZipInfo(path.removeprefix('bin/query/'),(2026,11,12,0,0,0))
                    info.external_attr = 0o100644<<16
                    bundle.writestr(info,source.read(prefix+path))
            data = stream.getvalue()
        assert len(data)==item['sizeBytes'],name
        assert hashlib.sha256(data).hexdigest()==item['sha256'],name
        dest = work/name
        dest.write_bytes(data)
        paths.append(str(dest))
    # Never mutate assets belonging to an already published resource release.
    found = subprocess.run(['gh','release','view',tag,'--repo',repo,'--json','isDraft'],capture_output=True,text=True)
    if found.returncode == 0:
        assert json.loads(found.stdout)['isDraft'], 'Release already published; choose a new resource tag'
    else:
        gh('release','create',tag,'--repo',repo,'--target',os.environ['GITHUB_SHA'],
           '--title','Resource Library - 2026-11-12','--notes',
           'Resource files imported from shDeveloperPack; this is NOT an application update. See content/migrations/2026-11-12/ for provenance and checks. Programs and SQL were not executed.',
           '--draft','--prerelease','--latest=false')
    # Upload in small batches. A failed run leaves only an unpublished draft.
    for offset in range(0,len(paths),15):
        gh('release','upload',tag,*paths[offset:offset+15],'--repo',repo,'--clobber')
    release = json.loads(gh('api',f'repos/{repo}/releases/tags/{tag}'))
    # --paginate concatenates arrays; --slurp wraps them for reliable JSON.
    pages = json.loads(gh('api','--paginate','--slurp',f'repos/{repo}/releases/{release["id"]}/assets?per_page=100'))
    remote = {a['name']:a for page in pages for a in page}
    assert len(remote)==len(manifest['assets'])
    for item in manifest['assets']:
        asset = remote[item['fileName']]
        assert asset['state']=='uploaded' and asset['size']==item['sizeBytes']
        assert asset.get('digest')=='sha256:'+item['sha256'],item['fileName']
    gh('release','edit',tag,'--repo',repo,'--draft=false','--prerelease','--latest=false')
    latest = json.loads(gh('api',f'repos/{repo}/releases/latest'))
    assert not latest['tag_name'].startswith('resources-'), 'Resource release must never be latest app version'
    print(f'Published {len(paths)} verified assets. Latest app release remains {latest["tag_name"]}.')
