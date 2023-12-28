# Vorislik polimorfizm
class Shaxs:
    def __init__(self,ism,familiya,manzili,telefon) -> None:
        self.ism=ism
        self.familiya=familiya
        self.manzili=manzili
        self.telefon=telefon
    def __repr__(self) -> str:
        return f'nomi : {self.nomi}\nfamiliyasi : {self.familiya}\n'
    def get_info(self):
        return f'nomi : {self.nomi}\nmanzili : {self.manzili}\n'
    def __call__(self):
        return self.manzili
class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,manzili,telefon,yoshi,) -> None:
        super().__init__(ism,familiya,manzili,telefon)
        self.yoshi=yoshi
    def get_info(self):
        s= super().get_info()
        s+=f'yoshi : {(self.yoshi)}\n'
        return s
class Admin(Foydalanuvchi):
    def __init__(self, ism,familiya, manzili, telefon, yoshi) -> None:
        super().__init__(ism,familiya,manzili, telefon, yoshi)
    def ban_user(self):
        return f'Foydalanuvchi bloklandi :\nismi : {self.ism}\nfamiliyasi : {self.familiya}\n'
a=Admin('Shohjahon','Atoboyev','Xiva','+998911231213',19)
print(a.ban_user())