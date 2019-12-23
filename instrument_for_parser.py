# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from requests import request
from _selectors import Selectors as sel
class InstrumentForParser():

    def get_request(self):#Завантажуєм сторінку
        active_t = request('GET', self ).text
        return(active_t)

    def soup(self):#Получаєм об'єкт супа
        active_t = InstrumentForParser.get_request(self)
        soup = BeautifulSoup(active_t, 'lxml')
        return soup

    def number_all_links(self):#Ітератор
        soup=InstrumentForParser.soup(self)
        return(len(soup.find_all('li', class_='info-lastpost')))

    def active_temes(self):#Повертає масив з даними останніх редагованих тем
        soup=InstrumentForParser.soup(self)
        topic_mas = []
        line_mas = []
        for number in range(InstrumentForParser.number_all_links(self)):
            text = str(soup.select(sel.find_today_elelments(number)))
            title = str(soup.select(sel.find_active_temes_url(number)))
            autor = str(soup.select(sel.find_last_autor_name(number)))
            if text[-22:-14] == "Сьогодні":
                line_mas.append(text[10:-24])#url
                line_mas.append(text[-13:-5])#time
                line_mas.append(autor[11:-8])
                line_mas.insert(0,(autor[11:-8]+text[-14:-5]))
                line_mas.append(InstrumentForParser. return_title(title[:-5]))
                topic_mas.append(line_mas)
                line_mas=[]
        return(topic_mas)

    def return_title(self):

        title=''
        for liter in self[::-1]:
            if liter == ">":
                return (title[::-1])
                break
            title += liter
        return(title[::-1])


