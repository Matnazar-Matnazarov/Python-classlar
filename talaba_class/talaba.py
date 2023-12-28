class talaba:
    def __init__(self, ism, familiya, guruh, shartnoma_turi) -> None:
        self.ism = ism
        self.familiya = familiya
        self.guruh = guruh
        self.shartnoma_turi = shartnoma_turi
        self.bosqich = 0
        self.fanlar = []
    def get_info(self):
        return f'ism: {self.ism}\nfamiliya: {self.familiya}\nguruh: {self.guruh}\nshartnoma turi: {self.shartnoma_turi}\nfanlar: {self.fanlar}\n'
    def fanla_yozildi(self, s):
        self.fanlar.append(s)
    def remove_fan(self, s):
        if s in self.fanlar:
            self.fanlar.remove(s)
        else:
            print('Siz bu fanga yozilmagansiz')
class fanlar:
    def __init__(self, fanla) -> None:
        self.fanla = fanla
    def __repr__(self) -> str:
        return self.fanla
ta = talaba('Matnazar', 'Matnazarov', '941-22', 'kontrakt')
a = fanlar("Ma'lumotlar bazasi")
b = fanlar("Ma'lumotlar tuzilmasi")
ta.fanla_yozildi(a)
ta.fanla_yozildi(b)
print(ta.get_info())
ta.remove_fan(b)
print(ta.get_info())