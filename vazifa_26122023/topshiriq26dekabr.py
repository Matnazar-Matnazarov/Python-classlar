# 1
class ishchi:
    def __init__(self,ism,guruh_raqami,staji) -> None:
        self.ism=ism
        self.guruh_raqami=guruh_raqami
        self.staji=staji
    def __repr__(self) -> str:
        return f'ism : {self.ism}\nguruh_raqami : {self.guruh_raqami}\nstaji : {self.staji}\n'
class korxona:
    def __init__(self,nomi,firma_raqami,manzil) -> None:
        self.nomi=nomi
        self.firma_raqami=firma_raqami
        self.manzil=manzil
        self.ishchilar=[]
    def get_info(self):
        s=""
        for i in self.ishchilar:
            s+=str(i)+'\n'
        return s
    def add_ishchi(self,s):
        self.ishchilar.append(s)
# 2
class mahsulot:
    def __init__(self,nomi,narxi,mamlakat) -> None:
        self.nomi=nomi
        self.narxi=narxi
        self.mamlakat=mamlakat
        self.soni=3
    def __repr__(self) -> str:
        return f'nomi : {self.nomi}\nnarxi : {self.narxi}\nmamlakat : {self.mamlakat}\n'
class dukon:
    def __init__(self,nomi,manzil,turi) -> None:
        self.nomi=nomi
        self.manzil=manzil
        self.turi=turi
        self.mahsulotlar=[]
    def add_mahsulotlar(self,s):
        self.mahsulotlar.append(s)
    def get_info(self):
        s=""
        for i in self.mahsulotlar:
            s+=str(i)+'\n'
        return s
# 3
class tikuvchi:
    def __init__(self,ism,familiya,lavozim,staji) -> None:
        self.ism=ism
        self.familiya=familiya
        self.lavozim=lavozim
        self.staji=staji
    def __repr__(self) -> str:
        return f'ism : {self.ism}\nfamiliya : {self.familiya}\nlavozim : {self.lavozim}\nstaji : {self.staji}\n'
class tikuvchiliksexi:
    def __init__(self,nomi,boshliq,ishchilar_soni) -> None:
        self.nomi=nomi
        self.boshliq=boshliq
        self.ishchilar_soni=ishchilar_soni
        self.tikuvchilar=[]
    def get_info(self):
        s=""
        for i in self.tikuvchilar:
            s+=str(i)+'\n'
        return s
    def add_tikuvchilar(self,s):
        self.tikuvchilar.append(s)
# 4
class shahar:
    def __init__(self,shahar_nomi,xuquqiy_holat) -> None:
        self.shahar_nomi=shahar_nomi
        self.xuquqiy_holat=xuquqiy_holat
    def __repr__(self) -> str:
        return f'shahar_nomi : {self.shahar_nomi}\nxuquqiy_holat : {self.xuquqiy_holat}\n'
class viloyat:
    def __init__(self,nomi,yer_maydoni,aholi_soni,respublika) -> None:
        self.nomi=nomi
        self.yer_maydoni=yer_maydoni
        self.aholi_soni=aholi_soni
        self.respublika=respublika
        self.shaharlar=[]
    def add_shaharlar(self,s):
        self.shaharlar.append(s)
    def get_info(self):
        s=""
        for i in self.shaharlar:
            s+=str(i)+'\n'
        return s
# 5
class futbolchi:
    def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni) -> None:
        self.ismi=ismi
        self.yoshi=yoshi
        self.kim_bolib_oynaydi=kim_bolib_oynaydi
        self.gollar_soni=gollar_soni
    def __repr__(self) -> str:
        return f'ismi : {self.ismi}\nyoshi : {self.yoshi}\nkim_bolib_oynaydi : {self.kim_bolib_oynaydi}\ngollar_soni : {self.gollar_soni}\n'
class jamoa:
    def __init__(self,nomi,yutuqlar_soni,yutqazishlar_soni) -> None:
        self.nomi=nomi
        self.yutuqlar_soni=yutuqlar_soni
        self.yutqazishlar_soni=yutqazishlar_soni
        self.futbolchilar=[]
    def get_info(self):
        s=""
        for i in self.futbolchilar:
            s+=str(i)+'\n'
        return s
    def add_futbolchilar(self,s):
        self.futbolchilar.append(s)
# 6
class ustoz:
    def __init__(self,ismi,yoshi,maktabi,sinf) -> None:
        self.ismi=ismi
        self.yoshi=yoshi
        self.maktabi=maktabi
        self.sinf=sinf
    def __repr__(self) -> str:
        return f'ismi : {self.ismi}\nyoshi : {self.yoshi}\nmaktabi : {self.maktabi}\nsinfi : {self.sinf}\n'
class maktab:
    def __init__(self,nomi,raqami,manzil,darajasi) -> None:
        self.nomi=nomi
        self.raqami=raqami
        self.manzil=manzil
        self.darajasi=darajasi
        self.ustozlar=[]
    def add_ustozlar(self,s):
        self.ustozlar.append(s)
    def get_info(self):
        s=""
        for i in self.ustozlar:
            s+=str(i)+'\n'
        return s