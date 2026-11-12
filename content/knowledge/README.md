# Knowledge library / Bilgi merkezi

Uygulama `content/knowledge/catalog.json` adresini okur. Başlangıç koleksiyonu 7 kategori, 41 yazı ve 33 kaynak içerir. Yeni yazılar ve düzeltmeler için EXE sürümünü değiştirmek gerekmez: JSON'u kaydedin, uygulamada **Information → Refresh** seçin. Açık bir okuyucu o anki içeriğin kopyasını gösterir; yenilenen içeriği görmek için okuyucuyu kapatıp kategoriyi yeniden açın.

## İçerik kuralları

- Arayüzle uyumlu olarak ilk koleksiyon İngilizcedir. Bir yazı, tüm oyunun veya tüm episode'ların eksiksiz belgesi değildir.
- Resmî ürün belgeleri, ilk elden açıklamalar, araç yazarlarının belgeleri ve incelenmiş dosyaları kullanın. Topluluk belgesini resmî oyun belgesi diye etiketlemeyin.
- Her yazıda `scope` ile bölge/episode/paket sınırını, `reviewedAt` ile gerçek kontrol tarihini belirtin. “Dosyada görüldü” ile “çalışırken test edildi” aynı şey değildir.
- `evidence` yalnızca `Source-backed overview`, `Inspected package` veya `Workflow guidance` olabilir. Bunlar doğruluk puanı değil, açıklamanın dayanağını gösterir.
- Kaynakların gerçekten desteklediği iddiaları yazın. Bulunmayan tarihleri, orijinal programlama dillerini, sabit portları ve GameVersion değerlerini tahmin etmeyin.
- Özel IP, parola, bağlantı sırrı veya oyuncu verisi eklemeyin. Örneklerin kapsamını ve gerekiyorsa izin gereksinimini belirtin.
- `code` alanı yalnızca okunabilen/kopyalanabilen örnektir; uygulama SQL veya komut çalıştırmaz. HTML, Markdown, script ve uzaktan XAML çalıştırılmaz; içerik düz metindir.

## Dosya yapısı

`schemaVersion` şu an `1`. `updatedAt` ve `reviewedAt` tarihleri `YYYY-MM-DD` biçimindedir.

`categories`: benzersiz `id`, görünen `name` ve kısa `description`.

`sources`: benzersiz `id`, `title`, kaynak türünü açıklayan `kind` ve doğrudan `https://` kaynak adresi. Bağlantıda kullanıcı adı/parola olamaz.

`articles`: benzersiz `id`, mevcut kategoriye ait `categoryId`, `title`, `summary`, `scope`, `evidence`, `reviewedAt`, `sourceIds` ve `blocks`. Her blokta `heading`, `body`, isteğe bağlı `code` bulunur. Her yazının en az bir geçerli kaynak referansı ve bir bloğu olmalıdır.

Yeni kaynak ekledikten sonra yazının `sourceIds` alanında bu kaynağın kimliğini kullanın. Yazılar JSON sırasıyla gösterilir; arama seçili kategoride başlık, özet ve bölüm metinlerini tarar. Mevcut kategori kimliklerini gereksiz yere değiştirmeyin.

Uygulama dosyayı kabul etmeden önce şemayı, kimlikleri, başvuruları, tarihleri, bağlantıları ve boyut sınırlarını doğrular. Hatalı bir yayın son geçerli önbelleği değiştirmez. İlk kullanımda internet gerekir; son başarılı içerik sonraki çevrim dışı kullanımlarda açılabilir.

## İnceleme kapsamı

`evidence/ep64-inspection.json` dosyası, incelenen EP6.4 arşivinin kaynak commit'ini, SHA-256 değerini, dosya yollarını ve yapılandırma anahtarlarını kaydeder. Özel değerler yayımlanmamıştır. Sunucu çalıştırılmamış, veritabanına bağlanılmamıştır.

Tarihçe, yapımcının 2008 tarihli röportajının bölgesel bağlamıyla sınırlıdır. Kore'deki kesin çıkış tarihi ve orijinal oyunun bütün teknoloji yığını bu ilk koleksiyonda doğrulanmış sayılmamıştır. shStudio/Parsec gibi araçların yetenekleri kendi yazarlarının belgelerine dayanır; kütüphanedeki her ikili sürümün davranışı test edilmiş değildir.

Kaynak kod deposunda `tests/Fixtures/knowledge.json` bu ilk koleksiyonun test kopyasıdır. Yayındaki içerik bununla sürekli eşit olmak zorunda değildir. Yeni şema özellikleri eklenirse okuyucunun ve testlerin de güncellenmesi gerekir.


## Çözüm durumu (0.1.11)

İsteğe bağlı `resolutionStatus` alanı boş bırakılabilir veya şu değerlerden birini alır:

- `Maintainer-confirmed fix`: aracın geliştiricisi düzeltmeyi bir sürümde açıkça yayımlamış.
- `Vendor-documented resolution`: üretici, bu hata ve koşullar için çözüm adımlarını belgelemiş.
- `Community-reported solution`: sorunun çözüldüğünü açıkça doğrulayan topluluk bildirimi var; doğrudan kaynak ve sürüm/paket bağlamı şart.

Etiket, kendi sunucumuzda test edildiği anlamına gelmez. `scope` ve yazı metni bu ayrımı açıklar. İlk genişlemede 3 geliştirici doğrulamalı düzeltme ve 2 Microsoft çözüm yazısı bulunur. Doğrulanmamış forum önerileri çözülmüş olarak eklenmedi. Yeni alan isteğe bağlı olduğundan 0.1.10 okuyucusu da kataloğu okuyabilir; eski sürüm ek durum etiketini göstermez.

Yeni eklenen 22 konu: sınıf listesi; blessing ve zorluk; Windows servis sağlığı; EP6.4 veritabanı anahtarları; MDF/NDF/LDF; test geri yükleme; VERIFYONLY sınırları; transactions; database roles; encoding; JSON düzenleme; harita düzenleme; workspace/patch; SHA-256; Git karşılaştırma; VS Code sürüm takibi; Parsec 1.1.1, 1.2.0 ve 1.1.0 düzeltmeleri; SQL 18456 ve 4064; çözüm etiketlerini okuma.
