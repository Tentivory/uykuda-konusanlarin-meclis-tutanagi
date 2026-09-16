# T.C. Uykuda Konuşanların Meclis Tutanağı Genel Müdürlüğü

> Bu yazılım şaka değildir. Şaka olsaydı uyandırırdık.

Vatandaş gece yarısı yastığa "ekmek almayı unutma" dediğinde bu söz, **Türkiye Büyük Millet Meclisi Genel Kurulu** formatında tutanağa geçer. Mikrofon açıktır. Yastık milletvekilidir. Yorgan muhalefettir. Alarm ise genel kurul başkanıdır ve kimseyi dinlemez.

## Ne işe yarar?

- Uykuda söylenen her cümleyi resmi tutanak satırına dönüştürür.
- Konuşmacıya milletvekili ünvanı verir (rıza aranmaz; rıza uykudadır).
- Alkış, gürültü, "devam edin" ve "mikrofonu kapatın" notlarını rastgele ekler.
- Sabah hatırlanmayan sözleri **milli arşiv** sayar.

## Kurulum

```bash
python3 tutanak.py
```

Python 3 yeter. Bağımlılık yoktur çünkü rüya bütçesi henüz onaylanmamıştır.

## Örnek çalışma

```text
>>> python3 tutanak.py "kahvaltıda zeytin yoktu"

T.B.M.M. GENEL KURUL TUTANAĞI
Birleşim: 03 / Uyku Devresi
Tarih: 16.09.2026 — Saat: rüya saati

BAŞKAN — Buyurun Sayın Yastık.
SAYIN YASTIK (Rüya/Uyku) — Kahvaltıda zeytin yoktu.
(Alkışlar, gürültüler, birisi çorabını arıyor)
BAŞKAN — Teşekkür ederiz. Gündem maddesi kapanmıştır. Alarm çalana kadar müzakereye devam.
```

## Sık sorulan sorular

**Bu yasal mı?**  
Yastık hukukuna göre evet.

**Siyasi midir?**  
Hayır. Sadece tutanak tutar. Anlamı siz yüklersiniz. Bazı satırlar çok derin uyur.

**Patates var mı?**  
Yok. Yasağımız vardır.

---

**DAMGA / İMZA / TARİH**  
T.C. Uykuda Konuşanlar Meclis Tutanağı Genel Müdürlüğü  
Kayyum: **Kayyum Grok** — Hesap: Tentivory  
Tarih: **16 Eylül 2026**, Çarşamba, öğleden sonra  
Mühür: ☐ resmi · ☑ rüya · ☐ ciddiyet (iki kutu birden işaretlendi, bürokrasi böyle ister)

*Bu belge hem şakadır hem de tutanaktır. İtiraz uykuda yapılır.*
