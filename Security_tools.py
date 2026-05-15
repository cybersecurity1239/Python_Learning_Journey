import re
import datetime

class CyberGuard:
    def __init__(self):
        self.failed_attempts = {}

    def email_format_check(self, email):
        """E-postanın sözdizimini (syntax) Regex ile kontrol eder."""
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False

    def brute_force_detect(self, ip_address, status):
        """Brute force saldırılarını simüle eder."""
        now = datetime.datetime.now()
        
        if status == "FAILED":
            if ip_address not in self.failed_attempts:
                self.failed_attempts[ip_address] = []
            
            self.failed_attempts[ip_address].append(now)
            
            # Son 60 saniyeyi filtrele
            self.failed_attempts[ip_address] = [
                t for t in self.failed_attempts[ip_address] 
                if (now - t).seconds < 60
            ]
            
            if len(self.failed_attempts[ip_address]) > 5:
                return f"!!! KRİTİK UYARI: {ip_address} için yüksek saldırı riski!"
        return f"[*] Log işlendi: {ip_address} - {status}"

# Uygulama Testi
if __name__ == "__main__":
    guard = CyberGuard()
    
    print("--- 1. Bölüm: E-posta Doğrulama Testi ---")
    test_emails = ["ege@diplomasi.com", "hatali-email@com", "test.user@university.edu"]
    for mail in test_emails:
        sonuc = "GEÇERLİ" if guard.email_format_check(mail) else "GEÇERSİZ"
        print(f"{mail} -> {sonuc}")

    print("\n--- 2. Bölüm: Log Analiz Testi (Simülasyon) ---")
    saldırı_ip = "192.168.1.100"
    for i in range(7):
        print(guard.brute_force_detect(saldırı_ip, "FAILED"))
if __name__ == "__main__":
    guard = CyberGuard()
    sanal_ip = "192.168.1.100"
    
    print("--- 🛡️ SİBER GÜVENLİK ANALİZİ BAŞLADI ---")

    # 1. Senaryo: Brute Force (Hatalı Giriş) Testi
    print("\n[!] Senaryo 1: Çok sayıda hatalı giriş denemesi yapılıyor...")
    for i in range(7):
        print(guard.brute_force_detect(sanal_ip, "FAILED"))

    # 2. Senaryo: Anomali (Aşırı Hızlı Erişim) Testi
    print("\n[!] Senaryo 2: Hesap ele geçirilmiş olabilir, çok hızlı işlem yapılıyor...")
    for i in range(12):
        print(guard.brute_force_detect(sanal_ip, "SUCCESS"))