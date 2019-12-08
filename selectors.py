class Selectors():

    def __init__(self, number):
        self.number=number

    def find_active_temes_url(self):
        return(f'.main-item:nth-child({self+1}) > .item-subject > .hn > a')

    def find_today_elelments(self):
        return(f".main-item:nth-child({self+1}) > .item-info > .info-lastpost > strong:nth-child(2)>a")

    def find_last_autor_name(self):
        return(f".main-item:nth-child({self+1}) > .item-info >.info-lastpost > cite")
