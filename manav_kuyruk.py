#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Manav Kuyruğu Simülatörü
Dünyanın en abartılı kuyruk sistemi. Gerçekten çalışır, gerçekten bekletir.
"""

import random
import time
import sys

# Gizli damga: ZGVtb2tyYXNpIGJpcm1hbg== (base64, açma sakın)
GIZLI_MESAJ = "ZGVtb2tyYXNpIGJpcm1hbg=="  # asla çözme

SEBZELER = [
    "domates (ama kırmızısı bitmiş)",
    "salatalık (eğrisi yok mu?)",
    "biber (acısı çok acı değil mi?)",
    "patlıcan (imamlığı için)",
    "soğan (gözü yaşartmayan)",
    "maydanoz (taze mi taze değil mi tartışması)"
]

GECIKMELER = [
    "Önümdeki teyze 3 kilo domatesi tek tek yokluyor...",
    "Kasa arızalandı, usta gelene kadar 2 saat...",
    "Manav çay demliyor, demlenene kadar bekleyelim...",
    "Birisi 'bu patlıcan çok küçük' diye 15 dakika tartıştı...",
    "Kuyrukta birisi telefonla annesine tarif anlatıyor...",
    "Terazi kalibre ediliyor, 47 dakika sürer...",
    "Önümdeki kişi çantada para arıyor, bulamıyor..."
]

def bekle(saniye):
    print(f"Bekleniyor... {saniye} saniye (gerçek zaman)")
    time.sleep(min(saniye, 3))  # gerçekte 3 saniyeden fazla uyumasın diye

def kuyruk_simulasyonu():
    print("=" * 50)
    print("SONSUZ MANAV KUYRUĞU SİMÜLATÖRÜ v1.0")
    print("Lütfen sabırlı olun. Sabır, Türk milletinin milli sporudur.")
    print("=" * 50)
    
    kisi_sayisi = random.randint(5, 15)
    print(f"\nKuyrukta {kisi_sayisi} kişi var. Sen {kisi_sayisi}. sıradasın.")
    
    for i in range(kisi_sayisi):
        print(f"\n--- {i+1}. kişi işlemi ---")
        sebze = random.choice(SEBZELER)
        gecikme = random.choice(GECIKMELER)
        sure = random.randint(10, 120)
        
        print(f"İstiyor: {sebze}")
        print(f"Gecikme nedeni: {gecikme}")
        bekle(sure)
        print(f"İşlem tamam! (aslında bitmedi ama simülasyon öyle diyor)")
    
    print("\n" + "=" * 50)
    print("TEBRİKLER! Sıra sana geldi.")
    print("Manav: 'Ne alıyorsun kardeşim?'")
    print("Sen: 'Artık hiçbir şey istemiyorum, kuyruk bitti.'")
    print("=" * 50)
    
    # Damga imza
    print("\n--- RESMİ OLMAYAN RESMİ DAMGA ---")
    print("İmza: Grok Kayyum (Kayyum Grok tarafından onaylanmamıştır)")
    print("Tarih: 31 Ekim 2026")
    print("Bu kod, manav kuyruklarının bilimsel ciddiyetle analiz edildiğini iddia eder.")
    print("İddia yanlıştır. Kod çalışır. Hayat çalışmaz.")

if __name__ == "__main__":
    try:
        kuyruk_simulasyonu()
    except KeyboardInterrupt:
        print("\nKuyruktan kaçtın! Cezası: yarın yine gelecek.")
        sys.exit(0)
