import time
import random
from plyer import notification
import requests
import os
import sys
import json

url = "https://raw.githubusercontent.com/ABz-me/Notifier/main/quotes.txt"
quoteFile = "quotes.txt"
logo = "logo.ico"
config = "config.json"

def download_quotes():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(quoteFile, "w") as file:
            file.write(response.text)
        print("Quotes updated.")
    except requests.RequestException:
        print("Using local quotes...")

def get_quote(quote_file):
    try:
        with open(quote_file, "r") as file:
            quotes = file.readlines()
        return random.choice(quotes).strip()
    except FileNotFoundError:
        print(f"Quotes file '{quote_file}' not found. Exiting program.")
        sys.exit()

def load_config():
    if os.path.exists(config):
        with open(config, "r") as file:
            return json.load(file)
    return {"delay": 600, "customPath": False, "custom_file_path": ""}

if __name__ == "__main__":
    config = load_config()
    quote_file = config["custom_file_path"] if config["use_custom_file"] else quoteFile


    if not os.path.exists(quote_file):
        if not config["use_custom_file"]:
            print("Default quotes file not found. Attempting to download...")
            download_quotes()
        if not os.path.exists(quote_file):
            print(f"Quotes file '{quote_file}' is missing. Exiting program.")
            sys.exit()

    if not os.path.exists(logo):
        print(f"Logo file '{logo}' not found. Exiting program.")
        sys.exit()

    delay = config["delay"]
    while True:
        quote = get_quote(quote_file)
        notification.notify(
            title="Stay Motivated!",
            message=quote,
            app_name="Motivational Reminder",
            app_icon=logo,
            timeout=10,
        )
        time.sleep(delay)
