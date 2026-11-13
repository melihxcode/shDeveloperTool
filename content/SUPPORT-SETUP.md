# shDeveloperTools destek sayfası kurulumu

Kontrol tarihi: 13 Kasım 2026. Uygulamadaki `$ Support the project` düğmesi hazırdır. Henüz bir hesap bağlantısı verilmediği için `content/support.json` içinde `enabled: false` bulunur. Bu durumda kullanıcıya hazırlık mesajı gösterilir, ödeme sayfası açılmaz.

## Önerilen başlangıç: Patreon

Yurt dışındaki kullanıcılar Patreon üzerinden destek olabilir. Patreon'un resmî ödeme tablosunda Türkiye / TRY yer alır. Bankaya ödeme Payoneer altyapısıyla işlenir; bu, ayrı bir Payoneer Wallet hesabı açmakla aynı şey değildir. Para kart numarasına değil banka hesabına aktarılır. Ziraat veya Enpara için kendi adınıza ait uygun hesabı ödeme kayıt ekranında tanımlayın; belirli bir bankanın kabulü ve hesabınızın onayı tamamlanmadan sorunsuz aktarım garantisi verilemez.

## Tek seferlik destek: Shop

Patreon'un belgelenmiş tek seferlik ödeme yöntemi **dijital ürün, gönderi veya koleksiyon satın almadır**; karşılıksız bağış düğmesi değildir. Tekrarlanan üyelik gerekmez.

1. Üretici sayfana geç; **Create → Product** seç.
2. Kendi hazırladığın gerçek bir dijital ürünü ekle: örneğin geliştirme kontrol listesi ve proje şablonları. Başkalarının arşivlerini destek ürünü olarak yeniden satma.
3. Başlık, içerik açıklaması ve önizlemeyi hazırla.
4. Tek seferlik fiyat belirle; resmî aralık **3–5.000 USD**. Başlangıç önerisi: 5 USD.
5. **Purchase only** seçeneğiyle yayımla. Ürün **Shop** bölümünde görünür.
6. Herkese açık ürün bağlantısını kopyala; oturum dışında açıp fiyatı ve içeriği kontrol et. Ziyaretçi **Buy** ile tek seferlik satın alır.
7. Bu bağlantıyı uygulamanın destek ayarına ekle. Aylık üyelik sayfasıyla karıştırma.

Ürün açıklaması önerisi: “An original developer checklist and project template pack. This is a one-time purchase supporting shDeveloperTools development. No recurring membership is required. The app's existing features remain free.” Yalnızca gerçekten teslim edeceğin içerikleri vaat et.

Standart platform kesintisi %10'dur; ödeme işleme, para çekme, döviz ve uygulanabilir vergiler ayrıca olabilir. Hesabındaki toplam ücretleri kontrol et.

## Türkiye'deki banka hesabına alma

**Settings → Creator settings → Billing and payouts → Add payout method** bölümünden gerçek ülkeni ve hesap türünü seç. Hesabına sunulan Türkiye banka transferi seçeneğiyle kendi adına Ziraat/Enpara hesabını tanımla; kimlik ve vergi adımlarını tamamla. Para kart numarasına değil banka hesabına gider. Sağlayıcı onayını, para birimini ve minimum çekim tutarını kontrol et; her banka hesabı için kabul garantisi yoktur. Banka bilgilerini yalnızca Patreon'un yönlendirdiği güvenli ödeme ekranında gir, uygulama JSON'una koyma.

## Uygulamada etkinleştirme

`content/support.json` dosyasında `provider` alanına `Patreon`, `url` alanına **size ait yayımlanmış ürün/Shop bağlantısını** yazın; doğruladıktan sonra `enabled` değerini `true` yapın. Sahte veya örnek profil kullanmayın. Bu dosyada yalnızca şema sürümü, etkinlik durumu, sağlayıcı adı ve herkese açık URL bulunur.

Uygulamada **Support → Refresh** ile yüklenir; EXE güncellemesi gerekmez. Ziyaretçi hedef adresi görür ve düğmeye basınca kendi tarayıcısında açar. Kart bilgileri uygulama tarafından toplanmaz. Devre dışı bırakmak için `enabled: false` kaydedin. Çevrimdışıyken daha önce kaydedilmiş ayarlar kullanılabileceği için eski ödeme bağlantısını da sağlayıcı tarafında yönetmeniz gerekir.

Desteklenen HTTPS alan adları: patreon.com / www.patreon.com, ko-fi.com / www.ko-fi.com, donate.bynogame.com, melihxcode.com / www.melihxcode.com. Alan adının teknik olarak kabul edilmesi, sağlayıcının Türkiye'de veya bu kullanım için uygun olduğunun onayı değildir.

ByNoGame'in Donate hizmeti aktif yayıncı izleyici desteğiyle sınırlı olduğundan, bağımsız bir yazılım projesi için otomatik olarak uygun kabul edilmedi. Başka bir sağlayıcı seçilirse önce kullanım amacı ve Türkiye ödeme uygunluğu kontrol edilmeli.

## Resmî kaynaklar

- [Patreon: ABD dışındaki üreticilere ödeme ve Türkiye/TRY tablosu](https://support.patreon.com/hc/en-gb/articles/39694936541965-Payout-guide-for-creators-outside-the-US)
- [Patreon: banka/ödeme bilgilerini ekleme](https://support.patreon.com/hc/en-us/articles/115004029783-Adding-your-payout-details)
- [Patreon: güncel ücretler](https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview)
- [ByNoGame: yayıncı hizmetinin kapsamı](https://donate.bynogame.com/live)

- [Patreon: tek seferlik satın alma](https://support.patreon.com/hc/en-us/articles/204606215-Can-I-make-a-one-time-payment)
- [Patreon: Shop ürünü yayımlama](https://support.patreon.com/hc/en-us/articles/16303719836813-Selling-one-time-purchases-on-Patreon)
