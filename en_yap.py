"""Türkçe index.html'den İngilizce en/index.html üretir; iki sayfanın SSS yapılandırılmış verisini de yeniler.

Kullanım: python3 en_yap.py   (site klasöründe)
Her çeviri satırı Türkçe sayfada beklenen sayıda geçmezse durur; Türkçe metin
değişince buradaki karşılığı da güncellenmeli. SSS verisi (FAQPage JSON-LD)
sayfadaki <details> sorularından üretilir, elle yazılmaz.
"""
import html
import json
import os
import re
import sys

KOK = os.path.dirname(os.path.abspath(__file__))
SITE = "https://mychakrahome.com.tr/"
VERI_BAS = '<script type="application/ld+json" id="sss-veri">'


def sss_verisi(sayfa, url, dil):
    bolum = re.search(r'<section class="sss".*?</section>', sayfa, re.S).group(0)
    ciftler = re.findall(r"<details(?: open)?>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>", bolum, re.S)
    if not ciftler:
        sys.exit("SSS bulunamadı")

    def duz(x):
        return html.unescape(re.sub(r"<[^>]+>", "", x)).strip()

    veri = {"@context": "https://schema.org", "@type": "FAQPage", "url": url, "inLanguage": dil,
            "mainEntity": [{"@type": "Question", "name": duz(q), "acceptedAnswer": {"@type": "Answer", "text": duz(a)}}
                           for q, a in ciftler]}
    return VERI_BAS + json.dumps(veri, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def veri_cikar(sayfa):
    return re.sub(re.escape(VERI_BAS) + r".*?</script>\n", "", sayfa, flags=re.S)


def veri_koy(sayfa, url, dil):
    return sayfa.replace("</head>", sss_verisi(sayfa, url, dil) + "\n</head>", 1)


s = veri_cikar(open(os.path.join(KOK, "index.html"), encoding="utf-8").read())
open(os.path.join(KOK, "index.html"), "w", encoding="utf-8").write(veri_koy(s, SITE, "tr"))

# (Türkçe, İngilizce, kaç kez geçmeli)
CEVIRI = [
    ('<html lang="tr">', '<html lang="en">', 1),
    ('<title>Jüt amerikan servis ve bardak altlığı setleri · Elle örülmüş</title>', '<title>Handwoven round jute placemat and coaster sets</title>', 1),
    ('content="Yuvarlak, elle örülmüş jüt amerikan servisler ve aynı renkte bardak altlıkları; toprak çömlekte kokulu mumlar ve çakıl taşı mumlar. Dört renk, 2\'li, 4\'lü ve 6\'lı setler. Satın alma Trendyol mağazamızda."',
     'content="Round, handwoven jute placemats with matching coasters; scented candles in terracotta pots and pebble candles. Four colours, sets for 2, 4 and 6. Available in our Trendyol store."', 1),
    ('<meta property="og:url" content="https://mychakrahome.com.tr/">', '<meta property="og:url" content="https://mychakrahome.com.tr/en/">', 1),
    ('<meta property="og:title" content="Jüt amerikan servis ve bardak altlığı setleri · Elle örülmüş">', '<meta property="og:title" content="Handwoven round jute placemat and coaster sets">', 1),
    ('<meta property="og:description" content="Dört renk, 2\'li, 4\'lü ve 6\'lı setler. Satın alma Trendyol mağazamızda.">', '<meta property="og:description" content="Four colours, sets for 2, 4 and 6. Available in our Trendyol store.">', 1),
    ('<meta property="og:image:alt" content="Mum ışığında ahşap masada tarçın kenarlı yuvarlak jüt servisler ve bardak altlıkları">', '<meta property="og:image:alt" content="Cinnamon-edged round jute placemats and coasters on a candlelit wooden table">', 1),
    ('<meta property="og:locale" content="tr_TR">', '<meta property="og:locale" content="en_GB">', 1),
    ('<meta property="og:locale:alternate" content="en_GB">', '<meta property="og:locale:alternate" content="tr_TR">', 1),
    ('<link rel="canonical" href="https://mychakrahome.com.tr/">', '<link rel="canonical" href="https://mychakrahome.com.tr/en/">', 1),
    ('href="favicon.svg"', 'href="../favicon.svg"', 1),
    ('href="stil.css"', 'href="../stil.css"', 1),
    ('src="site.js"', 'src="../site.js"', 1),
    ('src="img/', 'src="../img/', 18),
    ('<a class="dil" href="en/" hreflang="en" lang="en" aria-label="English">EN</a>', '<a class="dil" href="../" hreflang="tr" lang="tr" aria-label="Türkçe">TR</a>', 1),
    ('>İçeriğe geç<', '>Skip to content<', 1),
    ('Elle örülmüş jüt servisler ve mumlar · Siparişler <a href="https://www.trendyol.com/magaza/mychakra-home-m-473058" data-olay="trendyol-magaza" target="_blank" rel="noopener">Trendyol mağazamızda</a>, Trendyol güvencesiyle',
     'Handwoven jute placemats and candles · Orders through <a href="https://www.trendyol.com/magaza/mychakra-home-m-473058" data-olay="trendyol-magaza" target="_blank" rel="noopener">our Trendyol store</a> in Turkey', 1),
    ('aria-label="Menüyü aç"', 'aria-label="Open menu"', 1),
    ('aria-label="Ana menü"', 'aria-label="Main menu"', 1),
    ('aria-label="Ana sayfa"', 'aria-label="Home"', 2),
    ('>Jüt servisler<', '>Jute placemats<', 3),
    ('<a href="#mumlar">Mumlar</a>', '<a href="#mumlar">Candles</a>', 3),
    ('>Hikâyemiz<', '>Our story<', 3),
    ('>Sıkça sorulanlar<', '>FAQ<', 4),
    ('>İletişim<', '>Contact<', 4),
    ('<p class="etiket">Doğal jüt · Elle örülür</p>', '<p class="etiket">Natural jute · Handwoven</p>', 1),
    ('Sofranız için <em>elle örülmüş</em> jüt amerikan servisler.', '<em>Handwoven</em> jute placemats for your table.', 1),
    ('Yuvarlak amerikan servisler ve aynı renkte bardak altlıkları. Dört kenar rengi; iki, dört ve altı kişilik setler.', 'Round placemats with matching coasters. Four colours; sets for two, four and six.', 1),
    ('>Setleri inceleyin<', '>Explore the sets<', 1),
    ('<a class="yazi-bag" href="#mumlar">Mumlar <svg', '<a class="yazi-bag" href="#mumlar">Candles <svg', 1),
    ("Sınırlı sayıda · İngiltere'deki mağazamız için 2023'te üretildi", 'Limited stock · Made in 2023 for our shop in England', 1),
    ('alt="Mum ışığında ahşap masada dört kişilik akşam sofrası; tarçın kenarlı yuvarlak jüt servisler ve bardak altlıkları"', 'alt="Candlelit dinner for four on a wooden table, with cinnamon-edged round jute placemats and coasters"', 1),
    ("<figcaption>4'lü Tarçın set, akşam sofrasında</figcaption>", '<figcaption>Cinnamon set for 4, at dinner</figcaption>', 1),
    ('aria-label="Neden bu servisler"', 'aria-label="Why these placemats"', 1),
    ('<li><strong>Elle örülür</strong><span>Doğal jüt halattan, tek tek</span></li>', '<li><strong>Handwoven</strong><span>From natural jute rope, one by one</span></li>', 1),
    ('<li><strong>Rulo yapılır</strong><span>Çekmecede yer kaplamaz</span></li>', '<li><strong>Rolls up</strong><span>Takes little drawer space</span></li>', 1),
    ('<li><strong>Deri etiketli</strong><span>Kenarda damgalı “my” simgesi</span></li>', '<li><strong>Leather tag</strong><span>Stamped with our “my” mark</span></li>', 1),
    ("<li><strong>Trendyol güvencesi</strong><span>Ödeme, kargo ve iade Trendyol'da</span></li>", '<li><strong>Sold on Trendyol</strong><span>Payment, delivery and returns by Trendyol</span></li>', 1),
    ('alt="Tarçın: kiremit tonunda halat kenarlı yuvarlak jüt amerikan servis, üstten"', 'alt="Cinnamon: round jute placemat with a terracotta rope edge, from above"', 1),
    ('<p class="etiket">Dört renk</p>', '<p class="etiket">Four colours</p>', 1),
    ('Rengini <em>sofranıza</em> göre seçin.', 'Choose a colour for <em>your table</em>.', 1),
    ('<legend>Renk</legend>', '<legend>Colour</legend>', 1),
    ('</span>Tarçın</button>', '</span>Cinnamon</button>', 1),
    ('</span>Hardal</button>', '</span>Mustard</button>', 1),
    ('</span>Doğal</button>', '</span>Natural</button>', 1),
    ('<p class="secili-ad" id="seciliAd">Tarçın</p>', '<p class="secili-ad" id="seciliAd">Cinnamon</p>', 1),
    ('id="seciliTarif">Kiremit tonunda halat kenar. Ahşap masada ve toprak tonlu tabaklarla sıcak durur.<', 'id="seciliTarif">A terracotta rope edge. Warm on a wooden table and with earthy plates.<', 1),
    ('<dt>Servis</dt><dd id="seciliOlcu">Yaklaşık 36×34 cm, yuvarlak</dd>', '<dt>Placemat</dt><dd id="seciliOlcu">About 36×34 cm, round</dd>', 1),
    ('<dt>Set içeriği</dt><dd>Her sette servis kadar bardak altlığı (yaklaşık 9×9 cm)</dd>', '<dt>In the set</dt><dd>One coaster per placemat (about 9×9 cm)</dd>', 1),
    ('<dt>Malzeme</dt><dd id="seciliMalzeme">Doğal jüt halat, deri etiket</dd>', '<dt>Material</dt><dd id="seciliMalzeme">Natural jute rope, leather tag</dd>', 1),
    ("<p>Set boyunu seçin; Trendyol'daki ürün sayfası açılır.</p>", '<p>Pick a set size to open the product on Trendyol.</p>', 1),
    ("2'li set<small>2 kişilik</small>", 'Set of 2<small>for two</small>', 1),
    ("4'lü set<small>4 kişilik</small>", 'Set of 4<small>for four</small>', 1),
    ("6'lı set<small>6 kişilik</small>", 'Set of 6<small>for six</small>', 1),
    ('<p class="etiket">Set boyları</p>', '<p class="etiket">Set sizes</p>', 1),
    ('Kaç kişilik bir sofra?', 'How many at the table?', 1),
    ('Her sette servis kadar bardak altlığı var. Bütün setler dört renkte.', 'Every set has one coaster per placemat. All sets come in four colours.', 1),
    ('aria-label="Üstten masa çizimi: iki servis ve iki bardak altlığı"', 'aria-label="Table drawing from above: two placemats and two coasters"', 1),
    ('aria-label="Üstten masa çizimi: dört servis ve dört bardak altlığı"', 'aria-label="Table drawing from above: four placemats and four coasters"', 1),
    ('aria-label="Üstten masa çizimi: altı servis ve altı bardak altlığı"', 'aria-label="Table drawing from above: six placemats and six coasters"', 1),
    ("<h3>2'li set</h3>", '<h3>Set of 2</h3>', 1),
    ("<h3>4'lü set</h3>", '<h3>Set of 4</h3>', 1),
    ("<h3>6'lı set</h3>", '<h3>Set of 6</h3>', 1),
    ('2 servis + 2 bardak altlığı · 4 parça', '2 placemats + 2 coasters · 4 pieces', 1),
    ('4 servis + 4 bardak altlığı · 8 parça', '4 placemats + 4 coasters · 8 pieces', 1),
    ('6 servis + 6 bardak altlığı · 12 parça', '6 placemats + 6 coasters · 12 pieces', 1),
    ('<p>Tarçın, Hardal, Gold, Doğal</p>', '<p>Cinnamon, Mustard, Gold, Natural</p>', 3),
    ('alt="Tarçın kenarlı jüt servis, ahşap masada tabak ve çatal bıçakla"', 'alt="Cinnamon-edged jute placemat on a wooden table with plate and cutlery"', 1),
    ('alt="Hardal sarısı kenarlı jüt servis, ahşap masada tabak ve çatal bıçakla"', 'alt="Mustard-edged jute placemat on a wooden table with plate and cutlery"', 1),
    ('alt="Gold örgü jüt servisler, misafir akşam yemeği sofrasında"', 'alt="Gold braided placemats at a dinner table for guests"', 1),
    ('alt="Doğal jüt servis, ahşap masada tabak ve çatal bıçakla"', 'alt="Natural jute placemat on a wooden table with plate and cutlery"', 1),
    ('<h3>Tarçın</h3>', '<h3>Cinnamon</h3>', 1),
    ('<h3>Hardal</h3>', '<h3>Mustard</h3>', 1),
    ('<h3>Doğal</h3>', '<h3>Natural</h3>', 1),
    ("<span>2'li · 4'lü · 6'lı set</span>", '<span>Sets of 2 · 4 · 6</span>', 4),
    ('alt="Yakın çekim: sarmal örülmüş jüt halat, tarçın renkli halat kenar ve üzerinde “my” damgalı deri etiket"', 'alt="Close-up: spiral-woven jute rope, cinnamon rope edge and a leather tag stamped “my”"', 1),
    ('<p class="etiket">Yakından</p>', '<p class="etiket">Up close</p>', 1),
    ('Halat halat, <em>elle</em> örülür.', 'Woven <em>by hand</em>, rope by rope.', 1),
    ('<p>Her servis doğal jüt halattan elle örülür; halat ortadan dışa doğru sarmal ilerler. Kenardaki renkli halat setin rengini verir, deri etikette “my” simgemiz damgalıdır. El yapımı olduğu için parçalar arasında küçük ölçü ve örgü farkları olabilir.</p>',
     '<p>Each placemat is woven by hand from natural jute rope, spiralling out from the centre. The coloured rope on the edge gives the set its colour, and the leather tag carries our stamped “my” mark. Being handmade, pieces may vary slightly in size and weave.</p>', 1),
    ('<div><dt>Malzeme</dt><dd>Doğal jüt halat, deri etiket</dd></div>', '<div><dt>Material</dt><dd>Natural jute rope, leather tag</dd></div>', 1),
    ('<div><dt>Servis</dt><dd>Yaklaşık 36×34 cm (Tarçın, Gold), 35 cm (Hardal, Doğal)</dd></div>', '<div><dt>Placemat</dt><dd>About 36×34 cm (Cinnamon, Gold), 35 cm (Mustard, Natural)</dd></div>', 1),
    ('<div><dt>Bardak altlığı</dt><dd>Yaklaşık 9×9 cm, servisle aynı renkte</dd></div>', '<div><dt>Coaster</dt><dd>About 9×9 cm, same colour as the placemat</dd></div>', 1),
    ('<div><dt>Setler</dt><dd>2, 4 ve 6 kişilik</dd></div>', '<div><dt>Sets</dt><dd>For 2, 4 and 6</dd></div>', 1),
    ('alt="Elde rulo yapılmış tarçın kenarlı jüt servis"', 'alt="A cinnamon-edged jute placemat rolled up in hand"', 1),
    ('<p>Kullanmadığınızda rulo yapıp çekmeceye kaldırın.</p>', '<p>Roll it up and keep it in a drawer when not in use.</p>', 1),
    ('<p class="etiket">Sofrada</p>', '<p class="etiket">At the table</p>', 1),
    ('Sabah kahvaltısından akşam yemeğine.', 'From breakfast to dinner.', 1),
    ('alt="Pencere önünde ahşap masada kahvaltı: peynirli tost, çay ve tarçın kenarlı jüt servisler"', 'alt="Breakfast by the window: cheese toast, tea and cinnamon-edged jute placemats"', 1),
    ('<h3>Pazar kahvaltısı</h3>', '<h3>Sunday breakfast</h3>', 1),
    ('<p>Peynirli tost, demli çay, pencere önünde iki kişilik bir masa.</p>', '<p>Cheese toast, fresh tea, a table for two by the window.</p>', 1),
    ('alt="Salonda sehpa üstünde ahşap nihaleye konmuş çaydanlık, çay tabaklı ince belli bardaklar jüt altlıklarda"', 'alt="A Turkish teapot on a wooden trivet in the living room, tulip tea glasses on jute coasters"', 1),
    ('<h3>Çay saati</h3>', '<h3>Tea time</h3>', 1),
    ('<p>Sıcak demliği ve çaydanlığı jütün üzerine doğrudan koymayın; altına bir nihale yeter.</p>', '<p>Don’t put a hot teapot straight on the jute; a trivet underneath is enough.</p>', 1),
    ('alt="Tarçın kenarlı jüt servis ve bardak altlığı üzerinde su bardağı"', 'alt="A glass of water on a cinnamon-edged jute placemat and coaster"', 1),
    ('<h3>Bardak altlığıyla</h3>', '<h3>With coasters</h3>', 1),
    ('<p>Her sette servisle aynı renkte bardak altlıkları var.</p>', '<p>Every set comes with coasters in the same colour.</p>', 1),
    ('<p class="etiket">Mumlar</p>', '<p class="etiket">Candles</p>', 1),
    ('Toprak çömlekte <em>kokulu</em> mumlar.', '<em>Scented</em> candles in terracotta.', 1),
    ('<p>Toprak çömlek içinde dört kokuda mum; küçük, orta ve büyük boy ya da üçü bir arada. Yanında sofraya taş dokusu getiren kokusuz çakıl taşı mumlar.</p>',
     '<p>Candles in terracotta pots in four scents; small, medium and large, or all three together. Plus unscented pebble candles that bring a stone texture to the table.</p>', 1),
    ('alt="Üç boyda toprak çömlek içinde beyaz kokulu mum"', 'alt="Scented white candles in terracotta pots, in three sizes"', 1),
    ('<h3>Toprak çömlekte kokulu mum</h3>', '<h3>Scented candle in terracotta</h3>', 1),
    ("<p class=\"alt-baslik\">Kokuyu ve boyu seçin; Trendyol'da açılır.</p>", '<p class="alt-baslik">Pick a scent and size to open it on Trendyol.</p>', 1),
    ('alt="Salonda ahşap sehpa üstünde, taş tepside yanan gri çakıl taşı mum"', 'alt="A grey pebble candle burning on a stone tray on a wooden side table"', 1),
    ('<h3>Çakıl taşı mum</h3>', '<h3>Pebble candle</h3>', 1),
    ('<p class="alt-baslik">Kokusuz · Ø16 × 7 cm · yaklaşık 30 saat</p>', '<p class="alt-baslik">Unscented · Ø16 × 7 cm · about 30 hours</p>', 1),
    ('<p class="mum-not">Yanan mumu gözetimsiz bırakmayın; mumluk ya da tabak üzerinde kullanın.</p>', '<p class="mum-not">Never leave a burning candle unattended; use it on a holder or plate.</p>', 1),
    ("İngiltere'deki mağazamız için ürettirdik. Şimdi <em>Türkiye'deki</em> sofralar için.", 'Made for our shop in England. Now for tables in <em>Turkey</em>.', 1),
    ("<p>2023'te İngiltere'deki ev dekorasyonu mağazamız için el yapımı jüt servisler ve mumlar ürettirdik. Bu koleksiyonu şimdi Türkiye'deki sofralar için Trendyol mağazamızda satışa sunuyoruz. Stok sınırlı.</p>",
     '<p>In 2023 we had handmade jute placemats and candles made for our home décor shop in England. We now offer this collection in Turkey through our Trendyol store. Stock is limited.</p>', 1),
    ('aria-label="“my” simgesi"', 'aria-label="“my” mark"', 1),
    ('Aklınıza takılanlar', 'Good to know', 1),
    ('<summary>Nereden satın alabilirim?</summary>', '<summary>Where can I buy?</summary>', 1),
    ("<p>Bütün ürünlerimiz Trendyol mağazamızda. Bu sayfadaki düğmeler sizi doğrudan ilgili ürünün Trendyol sayfasına götürür; ödeme, kargo ve iade Trendyol üzerinden, Trendyol'un koşullarıyla yapılır.</p>",
     '<p>All our products are sold in our Trendyol store in Turkey. The buttons on this page take you straight to each product on Trendyol; payment, delivery and returns are handled by Trendyol under its terms. For orders from outside Turkey, please write to us.</p>', 1),
    ('<summary>Setlerde neler var?</summary>', '<summary>What is in a set?</summary>', 1),
    ("<p>Her sette servis kadar bardak altlığı var. Örneğin 4'lü sette 4 yuvarlak jüt amerikan servis ve aynı renkte 4 bardak altlığı, toplam 8 parça.</p>",
     '<p>One coaster per placemat. The set of 4, for example, has 4 round jute placemats and 4 coasters in the same colour, 8 pieces in all.</p>', 1),
    ('<summary>Hangi renkler var?</summary>', '<summary>Which colours are there?</summary>', 1),
    ("<p>Dört renk: Tarçın (kiremit tonunda halat kenar), Hardal (hardal sarısı halat kenar), Gold (jüt ve altın iplikten balıksırtı örgü) ve Doğal (jütün kendi tonu). Her renk 2'li, 4'lü ve 6'lı sette var. Jüt doğal bir lif olduğu ve servisler elle örüldüğü için ton parçadan parçaya biraz farklı olabilir.</p>",
     "<p>Four colours: Cinnamon (terracotta rope edge), Mustard (mustard-yellow rope edge), Gold (herringbone braid of jute and gold thread) and Natural (the jute's own tone). Each colour comes in sets of 2, 4 and 6. Jute is a natural fibre and every placemat is woven by hand, so the tone may vary slightly from piece to piece.</p>", 1),
    ('<summary>Servislerin ölçüsü ne?</summary>', '<summary>How big are the placemats?</summary>', 1),
    ('<p>Tarçın ve Gold servisler yaklaşık 36×34 cm, Hardal ve Doğal yaklaşık 35 cm; bardak altlıkları yaklaşık 9×9 cm. El yapımı olduğu için küçük farklar olabilir.</p>',
     '<p>Cinnamon and Gold placemats are about 36×34 cm, Mustard and Natural about 35 cm; coasters are about 9×9 cm. Being handmade, sizes may vary slightly.</p>', 1),
    ('<summary>Sıcak demlik ya da tencere jütün üzerine konur mu?</summary>', '<summary>Can a hot teapot or pan go on the jute?</summary>', 1),
    ('<p>Doğrudan konmamalı. Sıcak demlik, çaydanlık ve tencerenin altına nihale koyun; yanan mumu da mumluk ya da tabak üzerinde kullanın.</p>',
     '<p>Not directly. Put a trivet under hot teapots and pans, and use burning candles on a holder or plate.</p>', 1),
    ('<summary>Nasıl saklanır?</summary>', '<summary>How do I store them?</summary>', 1),
    ('<p>Kullanmadığınızda rulo yapıp kuru bir çekmecede saklayabilirsiniz.</p>', '<p>Roll them up and keep them in a dry drawer when not in use.</p>', 1),
    ('<summary>Mumlar kaç saat yanar?</summary>', '<summary>How long do the candles burn?</summary>', 1),
    ('<p>Üreticinin verdiği bilgiye göre toprak çömlekteki mumlar küçük boyda yaklaşık 20, orta boyda 30, büyük boyda 40 saat; çakıl taşı mum yaklaşık 30 saat yanar. Süre kullanıma göre değişebilir.</p>',
     '<p>According to the maker, the candles in terracotta pots burn for about 20 hours (small), 30 hours (medium) and 40 hours (large); the pebble candle burns for about 30 hours. Burn time may vary with use.</p>', 1),
    ('<summary>Hediye olarak gönderebilir miyim?</summary>', '<summary>Can I send one as a gift?</summary>', 1),
    ("<p>Evet. Trendyol'da siparişi verirken teslimat adresine hediye edeceğiniz kişinin adını ve adresini yazmanız yeterli.</p>",
     "<p>Yes. When you order on Trendyol, simply enter the recipient's name and address as the delivery address.</p>", 1),
    ('<summary>Kargo ve iade nasıl işliyor?</summary>', '<summary>How do delivery and returns work?</summary>', 1),
    ("<p>Siparişler Trendyol üzerinden kargoya verilir; tahmini kargoya veriliş süresi her ürünün Trendyol sayfasında yazar. İade, Trendyol'un koşullarıyla Trendyol'daki sipariş sayfanızdan yapılır.</p>",
     "<p>Orders are shipped through Trendyol; the estimated dispatch time is shown on each product's Trendyol page. Returns follow Trendyol's terms and are made from your order page on Trendyol.</p>", 1),
    ('Bize yazın.', 'Write to us.', 1),
    ("<p>Ürünler, toplu sipariş ya da iş birliği için formu doldurun; e-postayla dönüş yapalım. Sipariş, kargo ve iade sorularınızı Trendyol'daki sipariş sayfanızdan da iletebilirsiniz.</p>",
     '<p>For questions about our products, bulk orders or collaborations, fill in the form and we will reply by email. Questions about an order, delivery or a return can also be sent from your order page on Trendyol.</p>', 1),
    ('<p>E-posta: <a', '<p>Email: <a', 1),
    ('<input type="hidden" name="_subject" value="Siteden yeni mesaj">', '<input type="hidden" name="_subject" value="Siteden yeni mesaj (İngilizce sayfa)">', 1),
    ('<label>Adınız<input', '<label>Your name<input', 1),
    ('<label>E-posta adresiniz<input', '<label>Your email<input', 1),
    ('<label>Mesajınız<textarea', '<label>Your message<textarea', 1),
    ('<summary>Kişisel verileriniz hakkında</summary>', '<summary>About your personal data</summary>', 1),
    ('<p>Formda yazdığınız ad, e-posta ve mesaj yalnızca size yanıt vermek için kullanılır; başka bir amaçla işlenmez ve satılmaz. Mesajınız FormSubmit hizmeti aracılığıyla e-postamıza iletilir. Verilerinizin silinmesini mychakrahome@gmail.com adresine yazarak isteyebilirsiniz. Veri sorumlusu: Özlem Turgut Sunar (şahıs işletmesi), Sancaktepe, İstanbul.</p>',
     '<p>The name, email and message you send are used only to reply to you; they are not used for anything else or sold. Your message reaches our inbox through the FormSubmit service. You can ask us to delete your data by writing to mychakrahome@gmail.com. Data controller: Özlem Turgut Sunar (sole proprietorship), Sancaktepe, Istanbul.</p>', 1),
    ('<button type="submit" class="dugme">Gönder</button>', '<button type="submit" class="dugme">Send</button>', 1),
    ('<p>Özlem Turgut Sunar (şahıs işletmesi) · Sancaktepe, İstanbul ·', '<p>Özlem Turgut Sunar (sole proprietorship) · Sancaktepe, Istanbul ·', 1),
    ('<p>Bu sitede satış yapılmaz; siparişler Trendyol üzerinden alınır.</p>', '<p>Nothing is sold on this site; orders are placed on Trendyol.</p>', 1),
    ('<h2 id="alt-urunler">Ürünler</h2>', '<h2 id="alt-urunler">Products</h2>', 1),
    ('<a href="#renk">Renkler</a>', '<a href="#renk">Colours</a>', 1),
    ('data-olay="trendyol-magaza" target="_blank" rel="noopener">Trendyol mağazamız</a>', 'data-olay="trendyol-magaza" target="_blank" rel="noopener">Our Trendyol store</a>', 1),
    ('<h2 id="alt-yardim">Yardım</h2>', '<h2 id="alt-yardim">Help</h2>', 1),
    ('<span>Fotoğrafların bir kısmı yapay zekâ ile hazırlanmıştır.</span>', '<span>Some photos were created with AI.</span>', 1),
]

hata = []
for tr, en, adet in CEVIRI:
    n = s.count(tr)
    if n != adet:
        hata.append(f"{n}≠{adet}: {tr[:80]}")
        continue
    s = s.replace(tr, en)
if hata:
    print("Çeviri tutmadı:\n  " + "\n  ".join(hata))
    sys.exit(1)

os.makedirs(os.path.join(KOK, "en"), exist_ok=True)
open(os.path.join(KOK, "en", "index.html"), "w", encoding="utf-8").write(veri_koy(s, SITE + "en/", "en"))
print("en/index.html yazıldı; SSS verisi iki sayfada yenilendi")
