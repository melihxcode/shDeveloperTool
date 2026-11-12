# shDeveloperTools destek sayfası kurulumu

Kontrol tarihi: 12 Kasım 2026. Uygulamadaki `$ Support the project` düğmesi hazırdır. Henüz bir hesap bağlantısı verilmediği için `content/support.json` içinde `enabled: false` bulunur. Bu durumda kullanıcıya hazırlık mesajı gösterilir, ödeme sayfası açılmaz.

## Önerilen başlangıç: Patreon

Yurt dışındaki kullanıcılar Patreon üzerinden destek olabilir. Patreon'un resmî ödeme tablosunda Türkiye / TRY yer alır. Bankaya ödeme Payoneer altyapısıyla işlenir; bu, ayrı bir Payoneer Wallet hesabı açmakla aynı şey değildir. Para kart numarasına değil banka hesabına aktarılır. Ziraat veya Enpara için kendi adınıza ait uygun hesabı ödeme kayıt ekranında tanımlayın; belirli bir bankanın kabulü ve hesabınızın onayı tamamlanmadan sorunsuz aktarım garantisi verilemez.

Patreon öncelikle **tekrarlanan üyelik desteğine** uygundur. Aylık desteği tek seferlik bağış gibi tanıtmayın. Uygulamada bir üyelik veya özellik kilidi eklenmedi; Patreon üyeliği yalnızca dışarıdaki destek yöntemi olur.

1. Patreon'da içerik üreticisi sayfanızı oluşturun. Ad olarak `melihxcode` veya `shDeveloperTools` kullanabilirsiniz.
2. Projeyi tanıtın; desteklerin rehber araştırması, bakım ve geliştirme çalışmalarına katkı olduğunu yazın. Mevcut özelliklerin destek ödemesi gerektirmediğini açıkça belirtin.
3. İsterseniz tek bir basit aylık destek seviyesi oluşturun. Tutarı, yenilenme sıklığını ve vaat ettiğiniz karşılıkları açık yazın.
4. **Settings → Creator settings → Billing and payouts → Add payout method** yolunu izleyin. Gerçek ikamet/ödeme ülkenizi Türkiye, doğru bireysel/işletme durumunu seçin.
5. Hesabınıza sunulan banka transferi seçeneğinde kendi banka bilgilerinizi sağlayın; yönlendirme ve kimlik/vergi bilgisi adımlarını tamamlayın. Bu bilgileri yalnızca sağlayıcının güvenli ekranında girin, GitHub'a veya uygulama JSON'una koymayın.
6. Ödeme yönteminin onayını, para birimini, kesintileri ve minimum çekim tutarını hesabınızda kontrol edin. İlk ekleme veya değişiklik sonrası bekleme süresi uygulanabilir.
7. Herkese açık profil sayfanızı yayımlayın. Yalnızca bu sayfanın HTTPS bağlantısını uygulama yapılandırmasına ekleyin.

Yeni üreticiler için resmî tabloda %10 platform ücreti yer alıyor; buna ödeme işleme, gerektiğinde döviz dönüşümü, para çekme ve uygulanabilir vergiler eklenebilir. Kesinti toplamını yalnızca %10 sanmayın. Türkiye'deki gelir/vergi durumunu kendi faaliyetiniz için mali müşavirle netleştirin.

## Uygulamada etkinleştirme

`content/support.json` dosyasında `provider` alanına `Patreon`, `url` alanına **size ait yayımlanmış profil bağlantısını** yazın; doğruladıktan sonra `enabled` değerini `true` yapın. Sahte veya örnek profil kullanmayın. Bu dosyada yalnızca şema sürümü, etkinlik durumu, sağlayıcı adı ve herkese açık URL bulunur.

Uygulamada **Support → Refresh** ile yüklenir; EXE güncellemesi gerekmez. Ziyaretçi hedef adresi görür ve düğmeye basınca kendi tarayıcısında açar. Kart bilgileri uygulama tarafından toplanmaz. Devre dışı bırakmak için `enabled: false` kaydedin. Çevrimdışıyken daha önce kaydedilmiş ayarlar kullanılabileceği için eski ödeme bağlantısını da sağlayıcı tarafında yönetmeniz gerekir.

Desteklenen HTTPS alan adları: patreon.com / www.patreon.com, ko-fi.com / www.ko-fi.com, donate.bynogame.com, melihxcode.com / www.melihxcode.com. Alan adının teknik olarak kabul edilmesi, sağlayıcının Türkiye'de veya bu kullanım için uygun olduğunun onayı değildir.

ByNoGame'in Donate hizmeti aktif yayıncı izleyici desteğiyle sınırlı olduğundan, bağımsız bir yazılım projesi için otomatik olarak uygun kabul edilmedi. Başka bir sağlayıcı seçilirse önce kullanım amacı ve Türkiye ödeme uygunluğu kontrol edilmeli.

## Resmî kaynaklar

- [Patreon: ABD dışındaki üreticilere ödeme ve Türkiye/TRY tablosu](https://support.patreon.com/hc/en-gb/articles/39694936541965-Payout-guide-for-creators-outside-the-US)
- [Patreon: banka/ödeme bilgilerini ekleme](https://support.patreon.com/hc/en-us/articles/115004029783-Adding-your-payout-details)
- [Patreon: güncel ücretler](https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview)
- [ByNoGame: yayıncı hizmetinin kapsamı](https://donate.bynogame.com/live)
