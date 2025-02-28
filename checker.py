import time
import requests
import telegram
from colorama import Fore, init

# Renklerin düzgün çalışması için colorama'yı başlatıyoruz
init(autoreset=True)

# Telegram bot token ve chat ID
bot_token = "8174419564:AAHYwxfnocl94BJp32lI_UcwrNWIs755HNo"  # Başka Telegram kanalının token'ı
chat_id = "7045128535"  # Fotoğrafların gönderileceği kanalın chat_id
bot = telegram.Bot(token=bot_token)

# Telegram bildirimi gönder
def send_telegram_photo(photo_url, caption=""):
    try:
        bot.send_photo(chat_id=chat_id, photo=photo_url, caption=caption)
        print("Telegram fotoğraf bildirimi gönderildi.")
    except Exception as e:
        print(f"Telegram hatası: {e}")

# Giriş işlemini deneme
def try_login(email, password):
    # Burada giriş işlemi yapılır, başarı durumunu kontrol edersiniz.
    # Örneğin, email ve şifre doğruysa başarılı giriş yapılır
    # Başarılıysa True, başarısızsa False döndürür
    if email == "correct_email" and password == "correct_password":
        return True
    else:
        return False

# Fotoğraf URL'sini alıp Telegram'a gönderme
def get_photo_url(email):
    # Fotoğraf URL'sini belirli bir email'e göre alabiliriz
    # Örneğin, basitçe bir URL döndürebiliriz.
    # Gerçek hayatta fotoğrafı alacağınız kaynak farklı olabilir.
    photo_url = "https://example.com/path_to_user_photo.jpg"  # Örnek fotoğraf URL'si
    return photo_url

# Ana fonksiyon
def main():
    print("Program başlatıldı.")  # Programın başladığını belirten mesaj
    file_path = r"E:\txtler\text.txt"  # Dosya yolunu doğru şekilde güncelleyin

    accounts = read_accounts(file_path)  # Hesap bilgilerini dosyadan oku

    if not accounts:  # Dosya okuma başarısız olduysa uyarı ver
        print(f"Hesaplar dosyası boş ya da okunamadı: {file_path}")
        return

    print("Dosyadaki hesaplar:")
    for line in accounts:  # Dosyadaki satırları yazdıralım
        print(line.strip())

    for line in accounts:
        parts = line.strip().split(":")  # E-posta ve şifreyi ayır
        if len(parts) == 2:
            email = parts[0]
            password = parts[1]

            print(f"Giriş yapılıyor: {email}")

            # Giriş yapmayı dene
            login_success = try_login(email, password)

            if login_success:
                success_message = f"Başarılı giriş: {email}:{password}"
                print(Fore.GREEN + success_message)  # Başarılı girişleri yeşil renkte yazdır

                # Fotoğraf URL'sini al ve gönder
                photo_url = get_photo_url(email)
                send_telegram_photo(photo_url, caption=f"Başarılı giriş: {email}")

            else:
                failure_message = f"Başarısız giriş: {email}:{password}"
                print(Fore.RED + failure_message)  # Başarısız girişleri kırmızı renkte yazdır

            # Hızlı işlem yapmamak için bekleme süresi
            time.sleep(0.1)  # 0.1 saniye bekleme

# Dosya okuma fonksiyonu
def read_accounts(file_path):
    try:
        print(f"Dosya okunuyor: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {file_path}")
        return []
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        return []

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")

