# Dosya kütüphanesini yönetme

Uygulamanın kaynak kodu `shDeveloperTools` özel deposunda kalır. Herkese açık indirme dosyaları ve katalog **melihxcode/shDeveloperTool** deposundadır. Yeni dosya eklemek için uygulamayı yeniden derlemek veya sürüm yükseltmek gerekmez: kataloğu kaydettikten sonra uygulamada **Files → Refresh** yeterlidir.

## Düzen

| Uygulamadaki bölüm | categoryId | Ek seçim |
| --- | --- | --- |
| Client & Server Files → Client Files | `client` | `episode`, ör. `Episode 5.4` |
| Client & Server Files → Server Files | `server` | `episode` |
| SQL Programs & Queries → SQL Programs | `sql-programs` | `bit`: `32-bit`, `64-bit` veya `ARM64` |
| SQL Programs & Queries → SQL Queries | `queries` | Yok |
| Editing & Developer Tools → Editing Programs | `editors` | Yok |
| Editing & Developer Tools → Developer Programs | `developer` | Yok |
| Design & Web → Interface | `interface` | Yok |
| Design & Web → Website | `website` | Yok |

GitHub klasörleri uygulama menülerini belirlemez; JSON içindeki `categoryId`, `episode` ve `bit` belirler. Bu yüzden büyük dosyalar için çok sayıda klasör açmaya gerek yoktur. Releases içinde dosya adlarının başına `client-`, `server-`, `editors-`, `queries-`, `website-` gibi kısa bir önek ekleyin. Görünen isim `name` alanında daha okunaklı olabilir. Client dosyalarında dil adını da belirtin: `Episode 5.4 Client - TR`.

## Yeni dosyaları yükleme: GitHub ekranında

1. [shDeveloperTool Releases](https://github.com/melihxcode/shDeveloperTool/releases) sayfasını açın, **Draft a new release** seçin.
2. **Choose a tag → Find or create a new tag** alanına `resources-2026-11-13` gibi yeni ve benzersiz bir etiket yazın. Target `main` kalabilir. Başlık örneği: `Resource Library - 2026-11-13`.
3. Dosyaları **Attach binaries by dropping them here or selecting them** alanına sürükleyin. Yüklemenin tamamlanmasını bekleyin. Çok sayıda ilişkili dosyayı tek ZIP olarak yükleyebilirsiniz; tekil `.sql` indirmeleri de desteklenir.
4. **Set as a pre-release** seçeneğini işaretleyin. **Set as the latest release** seçeneğini işaretlemeyin. Kaynak paketleri böylece uygulamanın kararlı sürüm güncellemelerine karışmaz. Sonra **Publish release** seçin.
5. Yayınlanan sürümün **Assets** listesindeki dosyaya sağ tıklayıp bağlantısını kopyalayın. Bağlantı şu biçimde olmalı: `https://github.com/melihxcode/shDeveloperTool/releases/download/resources-2026-11-13/editors-example-1.0.zip`. Release sayfasının adresini veya geçici imzalı yönlendirme adresini kullanmayın.
6. [content/files-catalog.json](https://github.com/melihxcode/shDeveloperTool/blob/main/content/files-catalog.json) dosyasını açın, kalem simgesine basın. `files` dizisine aşağıdaki gibi bir kayıt ekleyin; önceki kayıtla arasında virgül olmalı. `categories` listesini değiştirmek gerekmez.
7. **Commit changes** ile `main` dalına kaydedin. Uygulamada **Files → Refresh** seçin; dosyayı doğru kategoride bulun ve indirmeyi deneyin.

Her Release asset'i **2 GiB'den küçük** olmalıdır. Daha büyük dosyaları HTTPS üzerinden doğrudan dosya sunan, tercihen HTTP Range destekli bir sunucuya koyup `url` alanına o adresi yazabilirsiniz. Oturum açma, CAPTCHA veya HTML indirme sayfası gerektiren bağlantılar uygun değildir.

```json
{
  "id": "editors-example-1-0",
  "categoryId": "editors",
  "name": "Example Editor 1.0",
  "fileName": "editors-example-1.0.zip",
  "url": "https://github.com/melihxcode/shDeveloperTool/releases/download/resources-2026-11-13/editors-example-1.0.zip",
  "sizeBytes": 123456,
  "sha256": "BURAYA_DOSYANIN_GERCEK_64_KARAKTERLIK_SHA256_DEGERI"
}
```

Bu örnekteki URL, boyut ve SHA-256 yer tutucudur; doğrudan kataloğa yapıştırmayın. İndireceğiniz gerçek dosyanın değerlerini kullanın. Windows PowerShell ile:

```powershell
(Get-Item "C:\Dosyalar\editors-example-1.0.zip").Length
(Get-FileHash "C:\Dosyalar\editors-example-1.0.zip" -Algorithm SHA256).Hash.ToLowerInvariant()
```

`id` benzersiz ve kalıcı olsun; İngilizce harf, sayı, tire veya alt çizgi kullanın. `fileName` yol değil yalnızca dosya adı olsun. Client/server kaydına `"episode": "Episode 5.4"`, SQL programına `"bit": "64-bit"` ekleyin. Diğer kategorilerde bu alanları eklemeyin. Aynı dosyanın yeni sürümünü yeni dosya adı ve yeni kayıt kimliğiyle yayımlamak, yarım kalmış indirmelerin eski içerikle karışmasını önler. Yayımlanmış bir asset'in içeriğini aynı URL altında değiştirmeyin.

İçeriği zamanla değişen resmi `latest`/`aka.ms` bağlantılarında sabit `sizeBytes` ve `sha256` kullanmayın: alanları kaldırın veya `null` yapın. Sabit, sürümlendirilmiş dosyalarda gerçek boyut ve SHA-256 kullanılması önerilir.

## 12 Kasım 2026 aktarımı

- Eski katalogdaki 143 bağlantının tamamı kontrol edildi. 125 bağlantı dosya döndürdü; 18 bağlantıdan 2 SQL dosyası eski depodan kurtarıldı, kalan 16 kayıt eklenmedi.
- Eski depodaki 106 kaynak dosya ve 1 toplu SQL paketi [resources-2026-11-12](https://github.com/melihxcode/shDeveloperTool/releases/tag/resources-2026-11-12) sürümüne taşındı. Eski depodaki dosyalar silinmedi.
- 21 çalışan dış bağlantı kendi sunucusunda kaldı. Toplam katalog: 128 kayıt.
- SQL listesinde `Fix - …`, `Query - …` ve en başta `00 - Complete SQL Query Pack` adları kullanılıyor. İki Bankteller dosyası ayrı varyant olarak adlandırıldı.
- 6.3 etiketli ancak gerçek yolu EP6.4 olan server paketi `Episode 6.4` olarak düzeltildi. SQL Server 2012 için yanlış `R2` etiketi kaldırıldı. Değişken SSMS bağlantısı belirli bir eski SQL yılıyla etiketlenmedi.
- Eski Features bölümündeki 5 metin dosyası yeni bir menü açmadan Developer Programs içinde `EP5.4 Reference - …` adıyla saklandı.
- Ayrıntılı [kontrol raporu](migrations/2026-11-12/migration-report.json), [kaynak ve SHA-256 listesi](migrations/2026-11-12/resource-manifest.json) ve [eski depo lisansı](migrations/2026-11-12/shDeveloperPack-LICENSE.txt) kayıtlıdır. Kaynak arşivlerin içindeki lisanslar değiştirilmedi.

Kontrol kapsamı: taşınan dosyalar tam olarak indirildi, sabitlenmiş kaynak Git nesneleriyle eşleştirildi ve SHA-256 hesaplandı; ZIP dosyalarının CRC kontrolü yapıldı. Dış bağlantılar HTTP yanıtı, ilk 64 KiB dosya imzası ve bildirilen toplam boyutla kontrol edildi; büyük dış dosyalar bütünüyle indirilmedi. Programlar, kurulumlar ve SQL sorguları çalıştırılmadı; linkin çalışması programın güncel Windows sürümlerinde çalışacağını doğrulamaz.
