class Talaba:
    number = 0
    def __init__(self, ism, familiya, t_sanasi):
        self.ism = ism
        self.familiya = familiya
        self.t_sanasi = t_sanasi
        Talaba.number += 1
        self.id=Talaba.number
    def get_info(self):
        print(f'id : {self.id}\nism : {self.ism}\nfamiliya : {self.familiya}\nt_sanasi : {self.t_sanasi}')
Man = Talaba('Matnazar', 'Matnazarov', '2004')
Man.get_info()
Shoh = Talaba('Shohjahon', 'Ataboyev', '2004')
Shoh.get_info()