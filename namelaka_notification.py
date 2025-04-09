import requests
from bs4 import BeautifulSoup
import time
import telegram

# Telegram бот-токен та ID чату (отримати через @BotFather і @userinfobot)
TELEGRAM_TOKEN = '7891927169:AAE1MnZpzmyh6n0VH5db2zSqOsuKSDt3BXs'
TELEGRAM_CHAT_ID = '925288814'

# URL Namelaka
URL = 'https://expz.menu/box/QKhb/jQRV'

# Ініціалізація Telegram-бота
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def check_box():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        if "немає в наявності" not in soup.text.lower():
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Таємний бокс Namelaka доступний!")
        else:
            print("Ще немає в наявності.")
    except Exception as e:
        print(f"Помилка: {e}")

# Перевірка кожні 10 хвилин
while True:
    check_box()
    time.sleep(600)  # 600 секунд = 10 хв
