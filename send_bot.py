import telebot
import config
from data_base import SQLighte
import time
import schedule

bot = config.bot

def send_morning_message():
    db = SQLighte(config.database)
    rownumber = 0
    while True






schedule.every().day.at("9:00").do(send_morning_message)

while True:
    schedule.run_pending()
    time.sleep(1)

