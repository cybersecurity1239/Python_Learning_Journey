def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "0'a bölünemez!"
    return a / b


print("=== Python Hesap Makinesi ===")

while True:
    print("\nİşlem Seç:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("5 - Çıkış")

    secim = input("Seçimin: ")

    if secim == "5":
        print("Program kapatıldı.")
        break

    if secim in ["1", "2", "3", "4","5"]:
        if secim in ["1", "2", "3", "4"]:
           try:
            # Kullanıcıdan veri girişi alındığı an "güvenli bölge" başlıyor
            sayi1 = float(input("İlk sayı: "))
            sayi2 = float(input("İkinci sayı: "))
           except ValueError:
            # Eğer kullanıcı sayı yerine harf veya sembol girerse burası çalışır
            print("--- GÜVENLİK UYARISI: Sadece sayı girmelisiniz! ---")
            continue
            # Bu komut, aşağıdaki işlemleri yapmadan döngünün başına atar
        sayi1 = float(input("İlk sayı: "))
        sayi2 = float(input("İkinci sayı: "))

        if secim == "1":
            print("Sonuç:", toplama(sayi1, sayi2))

        elif secim == "2":
            print("Sonuç:", cikarma(sayi1, sayi2))

        elif secim == "3":
            print("Sonuç:", carpma(sayi1, sayi2))

        elif secim == "4":
            print("Sonuç:", bolme(sayi1, sayi2))
        elif secim =="5" :
            print("Sonuç:", bolme(sayi1,sayi2))
        
        else:
             print("Geçersiz seçim!")