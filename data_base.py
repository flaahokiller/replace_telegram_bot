# -*- coding: utf-8 -*-
import sqlite3


class SQLighte():

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()#open database

    def write_parsing_result(self, data):#Запис про нові події до бази данних
        numbers = range(len(data))
        with self.connection:
            for number in numbers:
                self.cursor.execute("INSERT INTO message_data Values(?,?,?,?,?,?)", (number, data[number][0], data[number][1], data[number][2], data[number][3], data[number][4]))
            self.connection.commit()

    def errase_db(self):
        self.cursor.execute('DELETE FROM message_data')
        self.connection.commit()

    def close(self):
        """ Закриваєм поточне з'єднання з БД """
        self.connection.close()
