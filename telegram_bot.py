# -*- coding: utf-8 -*-
from instrument_for_parser import InstrumentForParser as ifs #parsing active topic url
import telebot
import config
from data_base import SQLighte
import time
from kreate_message import CreateMessage





bot = config.bot


class ReplaceBot():


    @bot.message_handler(commands=['start'])
    def reply_to_start_message(message):
        db = SQLighte(config.database)
        id_=CreateMessage.return_id_new_user()
        reply_database = db.add_user_to_data_base(id_, message.from_user.id)#Передаєм базі юзер_ід корисиувача в телеграмі якщо користувача немає в базі функція  його додає та повертає True інакше функція повертає False

        if reply_database == True:
            bot.send_message(message.chat.id,"Вітаю тебе друже. Я ReplaceBot і я щодня буду тобі присилати інформацію про нові повідомлення на https://replace.org.ua - українськім форумі програмістів. Щоб відписатись з россилки введи команду '/goodbye_replace'")
            bot.send_message(message.chat.id, CreateMessage.create_first_message())

        if reply_database == False:
            bot.send_message(message.chat.id, f"Привіт {message.from_user.username}. Якщо ти не забув то я ReplaceBot і я щодня присилаю тобі сповіщення про нові повідомлення на https://replace.org.ua - українськім форумі програмістів . Надіюсь в тебе все гаразд. Ти завжди можеш відписатись з россилки ввівши команду '/goodbye_replace'.")
            bot.send_message(message.chat.id, CreateMessage.create_first_message())

    @bot.message_handler(commands=['goodbye_replace'])# Видалення користувача з списку розсилки
    def del_user_from_list_of_notifications(message):
        db = SQLighte(config.database)
        db.delete_any_user_data(message.from_user.id)#Видаляєм юзера.

if __name__=='__main__':
    bot.polling(none_stop = True)
