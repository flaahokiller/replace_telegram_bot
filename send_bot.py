# -*- coding: utf-8 -*-
from instrument_for_parser import InstrumentForParser as ifs #parsing active topic url
import telebot
import config
from data_base import SQLighte
import time
import schedule
from kreate_message import CreateMessage

bot = config.bot

def send_day_message():
    db = SQLighte(config.database)
    rownumber = 0
    while True:
        try:
            user=db.select_single_user(rownumber, "users")
            print(user, rownumber)
            rownumber += 1
            bot.send_message(user[1], CreateMessage.create_first_message())
        except TypeError:
            return None


def parsing():
    db = SQLighte(config.database)
    db.errase_db()
    db.write_parsing_result(ifs.active_temes(config.url))#Передаєм в базу спарсені данні

schedule.every(1).minutes.do(parsing)
schedule.every(180).minutes.do(send_day_message)

while True:
    schedule.run_pending()
    time.sleep(1)

