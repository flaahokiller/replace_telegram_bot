import datetime
import telebot
import config
from data_base import SQLighte



bot = config.bot
hour = datetime.datetime.now().hour

class ReplaceBot():


    @bot.message_handler(commands=['start'])
    def reply_to_start_message(message):
        db = SQLighte(config.database)
        reply_database = db.add_user_to_data_base(message.from_user.id)#Передаєм базі юзер_ід корисиувача в телеграмі якщо користувача немає в базі функція  його додає та повертає True інакше функція повертає False
        if reply_database == True:
            bot.send_message(message.chat.id,"Вітаю тебе друже. Я ReplaceBot і я щодня буду тобі присилати інформацію про нові повідомлення на https://replace.org.ua - українськім форумі програмістів. Щоб відписатись з россилки введи команду '/goodbye_replace'")
        if reply_database == False:
            bot.send_message(message.chat.id, f"Привіт {message.from_user.username}. Якщо ти не забув то я ReplaceBot і я щодня присилаю тобі сповіщення про нові домлення на https://replace.org.ua - українськім форумі програмістів . Надіюсь в тебе все гаразд. Ти завжди можеш відписатись з россилки ввівши команду '/goodbye_replace'. Але я")

    @bot.message_handler(commands=['goodbye_relace'])# Видалення користувача з списку розсилки
        db = SQLighte(config.database)
    def del_user_from_list_of_notifications(message)
if __name__=='__main__':
    bot.polling(none_stop = True)
