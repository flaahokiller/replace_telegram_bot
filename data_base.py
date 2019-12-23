# -*- coding: utf-8 -*-
import sqlite3
import config

class SQLighte():

    def __init__(self, database = config.database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()#open database

    def one_rowid_from_data_base(self, table, column  ):
        for row in self.cursor.execute(f"SELECT rowid, * FROM {table} ORDER BY {column}"):
            return row

    def write_parsing_result(self, data):#Запис про нові події до бази данних
        numbers = range(len(data))
        with self.connection:
            for number in numbers:
                self.cursor.execute("INSERT INTO message_data Values(?,?,?,?,?,?)", (number, data[number][0], data[number][1], data[number][2], data[number][3], data[number][4]))

    def errase_db(self):
        with self.connection:
            self.cursor.execute('DELETE FROM message_data')

    def add_user_to_data_base(self,id_, user_id):#Пробуєм записати нового юзера до бази данних...
        try:
            self.cursor.execute("INSERT INTO users VALUES (?,?)", (id_, user_id))
            return(True)
        except sqlite3.IntegrityError: # ...якщо юзер є в базі данних то ...
            return(False)

    def delete_any_user_data(self, user_id):# Видаляєм користувача з бази данних
        with self.connection :
            self.cursor.execute(f'DELETE FROM users WHERE user_id={user_id}')

    def select_single(self, rownumber, table):#Получаєм рядок з номером rownumber
        with self.connection:
            try:
                return self.cursor.execute(f'SELECT * FROM {table} WHERE id = ?', (rownumber,)).fetchall()[0]
            except IndexError:
                return(None)

    def select_single_user(self, rownumber, table):#Получаєм рядок з номером rownumber
        with self.connection:
            try:
                return self.cursor.execute(f'SELECT * FROM {table} WHERE id = ?', (rownumber,)).fetchall()[0]
            except IndexError:
                return(None)

    def select_single_for_time(self, message_time):#Получаєм рядок з датою
        with self.connection:
            try:
                return self.cursor.execute(f'SELECT * FROM {table} WHERE time = ?', (message_time,)).fetchall()[0]
            except IndexError:
                return(None)

    def __del__(self):#Зберігаєм зміни та закриваєм поточне з'єднання з БД """
        self.connection.commit()
        self.connection.close()

