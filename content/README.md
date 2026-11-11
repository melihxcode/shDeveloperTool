# shDeveloperTools online content

Uygulama 0.1.6 ve sonrasında bu klasördeki JSON dosyalarını çevrimiçi okur. Dosyayı GitHub üzerinde düzenleyip **Commit changes** yapın. Uygulamada ilgili sekmeyi açın veya **Refresh** seçin; CDN değişiklikleri birkaç dakika gecikmeli gösterebilir.

## Dosya listesi
`files-catalog.json` içindeki `files` dizisine kayıt ekleyin. Dosyanın kendisini Releases'e veya bir HTTPS dosya sunucusuna yükleyin; bu klasöre büyük dosya koymayın. Doğrudan indirme URL'si kullanın.

| Ana grup | categoryId | Ek alan |
| --- | --- | --- |
| Client & Server Files | client / server | episode |
| SQL Programs & Queries | sql-programs | bit: 32-bit / 64-bit / ARM64 |
| SQL Programs & Queries | queries | Yok |
| Editing & Developer Tools | editors / developer | Yok |
| Design & Web | interface / website | Yok |

Örnek (URL, boyut ve SHA256 gerçek değerlerle değiştirilmelidir):
```json
{
  "id": "sql-tool-x64-v1",
  "categoryId": "sql-programs",
  "name": "SQL Tool",
  "bit": "64-bit",
  "fileName": "sql-tool-x64.zip",
  "url": "https://downloads.example.com/sql-tool-x64.zip",
  "sizeBytes": null,
  "sha256": null
}
```

`id` benzersiz olmalıdır. Bilinen boyut byte cinsinden yazılır. SHA-256 gerçek 64 haneli dosya özetidir; PowerShell: `Get-FileHash .\\dosya.zip -Algorithm SHA256`. Bilinmeyen boyut ve özet null olabilir; dağıtımda doğru özet kullanılması önerilir.

## Güncelleme geçmişi
`version-notes.json` bir dizidir. Yeni kayıt:
```json
{
  "version": "0.1.6",
  "date": "2026-11-11",
  "title": "An always-current library",
  "changes": ["Online file catalog", "Offline cache"]
}
```
Her sürüm yalnızca bir kez yer almalıdır. Tarih YYYY-MM-DD olmalıdır. Notlar JSON verisidir; HTML veya çalıştırılabilir kod değildir.

## Önemli ayrım
Bu içerikleri güncellemek yeni EXE gerektirmez. Uygulama kodunu değiştirmek yine yeni sürüm yayınlamayı gerektirir. Bu dosya güncelleme paketi manifesti değildir; Velopack'in releases.win.json dosyasını elle değiştirmeyin.

Ağ kesilirse son geçerli kopya kullanılır. Bozuk JSON çalışan önbelleğin üstüne yazılmaz. Katalog henüz boş olduğundan uygulama sahte dosya göstermez.
