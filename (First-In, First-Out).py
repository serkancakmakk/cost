# Stok girişleri: (miktar, birim maliyet)
stok_girisleri = [
    (100, 10),  # 100 birim 10 TL'den alındı
    (50, 12),   # 50 birim 12 TL'den alındı
    (200, 11)   # 200 birim 11 TL'den alındı
]

# Satış miktarları
satislar = [
    105,   # İlk satış 105 birim

]


def fifo_hesaplama(stok_girisleri, satislar):
    toplam_maliyet = 0
    stok = stok_girisleri.copy()

    for satis in satislar:
        while satis > 0:
            miktar, birim_maliyet = stok[0]

            if miktar > satis:
                toplam_maliyet += satis * birim_maliyet
                stok[0] = (miktar - satis, birim_maliyet)
                satis = 0
            else:
                toplam_maliyet += miktar * birim_maliyet
                satis -= miktar
                stok.pop(0)

    return toplam_maliyet

# FIFOya göre toplam maliyetin hesaplanması
toplam_maliyet = fifo_hesaplama(stok_girisleri, satislar)
print(f"Toplam Maliyet (FIFO): {toplam_maliyet} TL")