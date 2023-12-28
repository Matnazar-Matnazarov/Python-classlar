# class kompyuter:
#     def __init__(self,nomi,turi) -> None:
#         self.nomi=nomi
#         self.turi=turi
#     def __repr__(self):
#         return (self.nomi)
# class kompyuterlar:
#     def __init__(self,) -> None:
#         self
# object1=kompyuter('hp','kuchli')

# print(object1)
class Avto:
    def __init__(self,model,rang,korobka,narx):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narx=narx
        self.kilometr=0
    def update_km(self,s):
        self.kilometr+=s
    def __repr__(self):
        return  f'Model : {self.model}\nrang : {self.rang}\nkorobka : {self.korobka}\nkm :{str(self.kilometr)}\nnarxi :{self.narx}\n'
class Avto_salon:
    def __init__(self,salon_nomi,manzil):
        self.salon_nomi=salon_nomi
        self.manzil=manzil
        self.sotuvdagi_avtomobillar=[]
    def add_sotuvdagi_avtomobillar(self,s):
        self.sotuvdagi_avtomobillar.append(s)
    def __repr__(self):
        s=""
        for i in self.sotuvdagi_avtomobillar:
            for j in i:
                s+=str(j)
        return s
object1=Avto('Neksiya 2','qora','avtomat','100 million\n')
object2=Avto('Cobalt','oq','avtomat','150 million')
object3=Avto_salon('Sofi','Malika bozor')
object3.add_sotuvdagi_avtomobillar((object1,object2))
print(object3)