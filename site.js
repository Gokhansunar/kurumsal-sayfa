(function () {
  var EN = document.documentElement.lang === "en";
  function t(tr, en) { return EN ? en : tr; }
  var TY = "https://www.trendyol.com/genel-markalar/";
  var KOD = {
    tarcin: { 2: "jut-amerikan-servis-bardak-altligi-seti-2-kisilik-el-yapimi-yuvarlak-supla-tarcin-kiremit-36x34-cm-p-1227607255", 4: "jut-amerikan-servis-bardak-altligi-seti-4-kisilik-el-yapimi-yuvarlak-supla-tarcin-kiremit-36x34-cm-p-1227635554", 6: "jut-amerikan-servis-bardak-altligi-seti-6-kisilik-el-yapimi-yuvarlak-supla-tarcin-kiremit-36x34-cm-p-1227639037" },
    hardal: { 2: "jut-amerikan-servis-bardak-altligi-seti-2-kisilik-el-yapimi-yuvarlak-supla-hardal-sari-35-cm-p-1227607963", 4: "jut-amerikan-servis-bardak-altligi-seti-4-kisilik-el-yapimi-yuvarlak-supla-hardal-sari-35-cm-p-1227636964", 6: "jut-amerikan-servis-bardak-altligi-seti-6-kisilik-el-yapimi-yuvarlak-supla-hardal-sari-35-cm-p-1227640167" },
    gold: { 2: "jut-amerikan-servis-bardak-altligi-seti-2-kisilik-altin-iplikli-orgu-yuvarlak-supla-gold-36x34-cm-p-1227608454", 4: "jut-amerikan-servis-bardak-altligi-seti-4-kisilik-altin-iplikli-orgu-yuvarlak-supla-gold-36x34-cm-p-1227637208", 6: "jut-amerikan-servis-bardak-altligi-seti-6-kisilik-altin-iplikli-orgu-yuvarlak-supla-gold-36x34-cm-p-1227642593" },
    dogal: { 2: "jut-amerikan-servis-bardak-altligi-seti-2-kisilik-el-yapimi-yuvarlak-supla-dogal-35-cm-p-1227609334", 4: "jut-amerikan-servis-bardak-altligi-seti-4-kisilik-el-yapimi-yuvarlak-supla-dogal-35-cm-p-1227643793", 6: "jut-amerikan-servis-bardak-altligi-seti-6-kisilik-el-yapimi-yuvarlak-supla-dogal-35-cm-p-1227641420" }
  };
  var JUT = {
    tarcin: { ad: t("Tarçın", "Cinnamon"), img: "kenar-tarcin.webp",
      tarif: t("Kiremit tonunda halat kenar. Ahşap masada ve toprak tonlu tabaklarla sıcak durur.", "A terracotta rope edge. Warm on a wooden table and with earthy plates."),
      olcu: t("Yaklaşık 36×34 cm, yuvarlak", "About 36×34 cm, round"), malzeme: t("Doğal jüt halat, deri etiket", "Natural jute rope, leather tag"),
      alt: t("Tarçın: kiremit tonunda halat kenarlı yuvarlak jüt amerikan servis, üstten", "Cinnamon: round jute placemat with a terracotta rope edge, from above") },
    hardal: { ad: t("Hardal", "Mustard"), img: "kenar-hardal.webp",
      tarif: t("Hardal sarısı halat kenar. Beyaz tabaklar ve açık renk masayla canlı bir sofra kurar.", "A mustard-yellow rope edge. Lively with white plates and light tables."),
      olcu: t("Yaklaşık 35 cm, yuvarlak", "About 35 cm, round"), malzeme: t("Doğal jüt halat, deri etiket", "Natural jute rope, leather tag"),
      alt: t("Hardal: hardal sarısı halat kenarlı yuvarlak jüt amerikan servis, üstten", "Mustard: round jute placemat with a mustard-yellow rope edge, from above") },
    gold: { ad: "Gold", img: "kenar-gold.webp",
      tarif: t("Jüt ve altın iplikten örgü kordon; yüzeyde balıksırtı desen. Işıkta hafifçe parlar, misafir ve yılbaşı sofralarına yakışır.", "Braided cord of jute and gold thread with a herringbone surface. A soft shine for guest and holiday tables."),
      olcu: t("Yaklaşık 36×34 cm, yuvarlak", "About 36×34 cm, round"), malzeme: t("Jüt ve altın iplikten örgü kordon", "Braided cord of jute and gold thread"),
      alt: t("Gold: altın sarısı örgü kordondan yuvarlak amerikan servis, üstten", "Gold: round placemat of braided jute and gold thread, from above") },
    dogal: { ad: t("Doğal", "Natural"), img: "kenar-dogal.webp",
      tarif: t("Doğal jüt tonunda, sade bir servis. Her tabak ve masa rengiyle uyum sağlar.", "A simple placemat in natural jute. Goes with any plate and table."),
      olcu: t("Yaklaşık 35 cm, yuvarlak", "About 35 cm, round"), malzeme: t("Doğal jüt halat, deri etiket", "Natural jute rope, leather tag"),
      alt: t("Doğal renk yuvarlak jüt amerikan servis, üstten", "Natural round jute placemat, from above") }
  };
  var C = "toprak-comlekte-kokulu-mum-";
  var K = t("Küçük", "Small"), O = t("Orta", "Medium"), B = t("Büyük", "Large"), S3 = t("3'lü set", "Set of 3");
  var MUM = [
    { k: "lavanta", ad: t("Lavanta", "Lavender"), boy: [[K, C + "kucuk-boy-lavanta-kokulu-dekoratif-mum-p-1227822652"], [O, C + "orta-boy-lavanta-kokulu-dekoratif-mum-p-1227823782"], [S3, C + "3-lu-set-kucuk-orta-buyuk-lavanta-kokulu-dekoratif-mum-p-1227652444"]] },
    { k: "vanilya", ad: t("Vanilya", "Vanilla"), boy: [[K, C + "kucuk-boy-vanilya-kokulu-dekoratif-mum-p-1227654646"], [O, C + "orta-boy-vanilya-kokulu-dekoratif-mum-p-1227833512"], [B, C + "buyuk-boy-vanilya-kokulu-dekoratif-mum-p-1227831944"], [S3, C + "3-lu-set-kucuk-orta-buyuk-vanilya-kokulu-dekoratif-mum-p-1227820990"]] },
    { k: "tarcin", ad: t("Tarçın", "Cinnamon"), boy: [[K, C + "kucuk-boy-tarcin-kokulu-dekoratif-mum-p-1227828860"], [O, C + "orta-boy-tarcin-kokulu-dekoratif-mum-p-1227820348"], [S3, C + "3-lu-set-kucuk-orta-buyuk-tarcin-kokulu-dekoratif-mum-p-1227829442"]] },
    { k: "amber", ad: "Amber", boy: [[K, C + "kucuk-boy-amber-kokulu-dekoratif-mum-p-1227819078"], [O, C + "orta-boy-amber-kokulu-dekoratif-mum-p-1227655878"], [B, C + "buyuk-boy-amber-kokulu-dekoratif-mum-p-1227827692"], [S3, C + "3-lu-set-kucuk-orta-buyuk-amber-kokulu-dekoratif-mum-p-1227821648"]] }
  ];
  var CAKIL = [
    [t("Gri", "Grey"), "cakil-gri", "cakil-tasi-mum-buyuk-boy-gri-kokusuz-dekoratif-mum-tas-gorunumlu-16x7-cm-yaklasik-30-saat-p-1227830264"],
    [t("Antrasit", "Anthracite"), "cakil-antrasit", "cakil-tasi-mum-buyuk-boy-antrasit-kokusuz-dekoratif-mum-tas-gorunumlu-16x7-cm-yaklasik-30-saat-p-1227822100"]
  ];
  var imgYol = EN ? "../img/" : "img/";

  function bag(metin, yol, urun, aciklama) {
    var a = document.createElement("a");
    a.href = TY + yol; a.textContent = metin; a.setAttribute("data-urun", urun);
    a.target = "_blank"; a.rel = "noopener";
    if (aciklama) a.setAttribute("aria-label", aciklama);
    return a;
  }
  function boyKodu(b) { return /^3/.test(b[1].split("mum-")[1]) ? "3lu" : b[1].split("mum-")[1].split("-boy")[0]; }
  function satir(ad, baglar) {
    var li = document.createElement("li");
    var s = document.createElement("strong"); s.textContent = ad; li.appendChild(s);
    var d = document.createElement("span"); d.className = "boylar-bag";
    baglar.forEach(function (b) { d.appendChild(b); });
    li.appendChild(d); return li;
  }
  var kokular = document.getElementById("kokular");
  MUM.forEach(function (m) {
    kokular.appendChild(satir(m.ad, m.boy.map(function (b) { return bag(b[0], b[1], "mum-" + m.k + "-" + boyKodu(b), m.ad + ", " + b[0] + t(", Trendyol'da aç", ", open on Trendyol")); })));
  });
  var cakil = document.getElementById("cakil");
  CAKIL.forEach(function (c) {
    cakil.appendChild(satir(c[0], [bag(t("Trendyol'da görün", "View on Trendyol"), c[2], c[1], c[0] + t(" çakıl taşı mum, Trendyol'da aç", " pebble candle, open on Trendyol"))]));
  });

  var hareketAz = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var sahne = document.getElementById("sahneGorsel");
  var dugmeler = Array.prototype.slice.call(document.querySelectorAll(".renk-dugme"));
  var boyBag = Array.prototype.slice.call(document.querySelectorAll("#boyDugmeler a"));

  function sec(anahtar) {
    var r = JUT[anahtar];
    if (!r) return;
    dugmeler.forEach(function (d) { d.setAttribute("aria-pressed", d.getAttribute("data-renk") === anahtar ? "true" : "false"); });
    document.getElementById("seciliAd").textContent = r.ad;
    document.getElementById("seciliTarif").textContent = r.tarif;
    document.getElementById("seciliOlcu").textContent = r.olcu;
    document.getElementById("seciliMalzeme").textContent = r.malzeme;
    boyBag.forEach(function (a) {
      var boy = a.getAttribute("data-boy");
      a.href = TY + KOD[anahtar][boy];
      a.setAttribute("data-urun", "jut-" + anahtar + "-" + boy);
      a.setAttribute("aria-label", r.ad + ", " + t(boy + " kişilik set, Trendyol'da aç", "set for " + boy + ", open on Trendyol"));
    });
    var yeni = imgYol + r.img;
    if (sahne.getAttribute("src") !== yeni) {
      sahne.src = yeni;
      sahne.alt = r.alt;
      if (!hareketAz && sahne.animate) {
        sahne.animate([
          { opacity: 0.2, transform: "rotate(-70deg) scale(0.94)" },
          { opacity: 1, transform: "rotate(0deg) scale(1)" }
        ], { duration: 750, easing: "cubic-bezier(.2,.7,.2,1)" });
      }
    }
  }
  // Ürün görme (TikTok ViewContent): yalnızca ziyaretçi bir renk seçince ya da reklamdan renkle gelince; piksel onayla yüklüyse.
  function izle(anahtar) {
    if (window.ttq && window.ttq.track && JUT[anahtar]) window.ttq.track("ViewContent", { contents: [{ content_id: "jut-" + anahtar, content_type: "product_group", content_name: JUT[anahtar].ad }] });
  }
  sec("tarcin");
  // Reklamdan gelen bağlantıda ?renk=gold gibi bir renk varsa o renk seçili açılır.
  var ilkRenk = null;
  try { ilkRenk = new URLSearchParams(location.search).get("renk"); if (ilkRenk && JUT[ilkRenk]) sec(ilkRenk); else ilkRenk = null; } catch (e) { ilkRenk = null; }
  dugmeler.forEach(function (d) { d.addEventListener("click", function () { sec(d.getAttribute("data-renk")); izle(d.getAttribute("data-renk")); }); });
  Array.prototype.forEach.call(document.querySelectorAll("[data-renk-sec]"), function (a) {
    a.addEventListener("click", function () { sec(a.getAttribute("data-renk-sec")); izle(a.getAttribute("data-renk-sec")); });
  });

  var menuDugme = document.getElementById("menuDugme");
  var mobilMenu = document.getElementById("mobilMenu");
  function menuKapat() { mobilMenu.hidden = true; menuDugme.setAttribute("aria-expanded", "false"); menuDugme.setAttribute("aria-label", t("Menüyü aç", "Open menu")); }
  menuDugme.addEventListener("click", function () {
    if (menuDugme.getAttribute("aria-expanded") === "true") { menuKapat(); return; }
    menuDugme.setAttribute("aria-expanded", "true");
    menuDugme.setAttribute("aria-label", t("Menüyü kapat", "Close menu"));
    mobilMenu.hidden = false;
  });
  Array.prototype.forEach.call(mobilMenu.querySelectorAll("a"), function (a) { a.addEventListener("click", menuKapat); });

  // Ziyaret ve Trendyol tıklaması ölçümü: Google Analytics 4 ve TikTok pikseli, yalnızca ziyaretçi onay verirse.
  var GA_ID = "G-CGK53N7DGH";
  var TT_ID = "DBKEBV3C77U0QK5QEL6G";
  var ANAHTAR = "cerez-onay-2";
  function oku() { try { return localStorage.getItem(ANAHTAR); } catch (e) { return null; } }
  function yaz(v) { try { localStorage.setItem(ANAHTAR, v); } catch (e) {} }
  function gaYukle() {
    if (!GA_ID || window.gtag) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_ID);
    var sc = document.createElement("script");
    sc.async = true; sc.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
    document.head.appendChild(sc);
  }
  function ttYukle() {
    if (!TT_ID || window.ttq) return;
    // TikTok'un verdiği piksel kodu (Etkinlik Yöneticisi, 03.11.2026); kimlik TT_ID'den gelir.
    !function (w, d, t) {
      w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(
      var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var r="https://analytics.tiktok.com/i18n/pixel/events.js",o=n&&n.partner;ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=r,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};n=document.createElement("script")
      ;n.type="text/javascript",n.async=!0,n.src=r+"?sdkid="+e+"&lib="+t;e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(n,e)};
      ttq.load(TT_ID);
      ttq.page();
    }(window, document, 'ttq');
  }
  function olcumYukle() { gaYukle(); ttYukle(); }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[data-urun], a[data-olay='trendyol-magaza']");
    if (!a) return;
    var urun = a.getAttribute("data-urun") || "magaza";
    if (window.gtag) window.gtag("event", "trendyol_tiklama", { urun: urun, dil: EN ? "en" : "tr", transport_type: "beacon" });
    if (window.ttq && window.ttq.track) window.ttq.track("ClickButton", { contents: [{ content_id: urun, content_type: "product", content_name: urun }], description: "Trendyol'da satın al" });
  });
  if (GA_ID || TT_ID) {
    var secim = oku();
    if (secim === "evet") { olcumYukle(); if (ilkRenk) izle(ilkRenk); }
    else if (secim !== "hayir") {
      var bant = document.createElement("div");
      bant.className = "cerez";
      bant.setAttribute("role", "region");
      bant.setAttribute("aria-label", t("Çerez tercihi", "Cookie choice"));
      var p = document.createElement("p");
      p.textContent = t("Hangi ürünlerin ilgi gördüğünü ve reklamlarımızın işe yarayıp yaramadığını anlamak için ölçüm çerezleri (Google Analytics ve TikTok pikseli) kullanmak istiyoruz. Kabul etmezseniz çerez kullanılmaz.", "We would like to use measurement cookies (Google Analytics and the TikTok pixel) to see which products people are interested in and whether our ads work. If you decline, no cookies are used.");
      var evet = document.createElement("button"); evet.type = "button"; evet.className = "dugme ince"; evet.textContent = t("Kabul et", "Accept");
      var hayir = document.createElement("button"); hayir.type = "button"; hayir.className = "dugme ince cerceve"; hayir.textContent = t("Reddet", "Decline");
      evet.addEventListener("click", function () { yaz("evet"); bant.remove(); olcumYukle(); if (ilkRenk) izle(ilkRenk); });
      hayir.addEventListener("click", function () { yaz("hayir"); bant.remove(); });
      var d = document.createElement("div"); d.className = "cerez-dugmeler"; d.appendChild(hayir); d.appendChild(evet);
      bant.appendChild(p); bant.appendChild(d);
      document.body.appendChild(bant);
    }
  }
})();
