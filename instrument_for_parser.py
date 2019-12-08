from bs4 import BeautifulSoup
from requests import request
from selectors import Selectors as sel
class InstrumentForParser():

    def __init__(self, url):
        self.link = url

    def get_request(self):#Download page
        active_t = request('GET', self ).text
        return(active_t)

    def soup(self):#soup objects
        active_t = InstrumentForParser.get_request(self)
        soup = BeautifulSoup(active_t, 'lxml')
        return soup

    def number_all_links(self):#Number of iteration
        soup=InstrumentForParser.soup(self)
        return(len(soup.find_all('li', class_='info-lastpost')))

    def active_temes(self):#return topic id
        soup=InstrumentForParser.soup(self)
        links_mas=[]
        titles_mas=[]
        times_mas=[]
        autors_mas=[]
        for number in range(InstrumentForParser.number_all_links(self)):
            text = str(soup.select(sel.find_today_elelments(number)))
            title = str(soup.select(sel.find_active_temes_url(number)))
            autor = str(soup.select(sel.find_last_autor_name(number)))
            if text[-22:-14] == "Сьогодні":
                links_mas.append(text[11:-34])
                titles_mas.append(InstrumentForParser.return_title(title[39:-5]))
                times_mas.append(text[-14:-5])
                autors_mas.append(autor[6:-7])
        return(links_mas, titles_mas, times_mas)

    def return_title(self):

        title=''
        for liter in self[::-1]:
            if liter == ">":
                return (title[::-1])
                break
            title += liter
        return(title[::-1])


