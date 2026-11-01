# mychakrahome.com.tr

Ürün vitrini (GitHub Pages). Satış yok: her ürün düğmesi Trendyol'daki ürün sayfasına gider.

- `index.html` Türkçe sayfa; `en/index.html` İngilizce sayfa, `python3 en_yap.py` ile Türkçeden üretilir (Türkçe metin değişince çeviri listesi de güncellenir).
- `stil.css`, `site.js` iki dilin ortak dosyaları. Ürünlerin Trendyol bağlantıları ve ürün kodları `site.js` içinde.
- Sayaç: Google Analytics 4, yalnızca ziyaretçi çerez onayı verirse yüklenir; Trendyol tıklamaları `trendyol_tiklama` olayı, `urun` parametresiyle.
- İletişim formu FormSubmit üzerinden e-postaya gelir.
