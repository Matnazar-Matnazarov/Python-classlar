class ishchi:
    def __init__(self,ism,firma,raqami,staji):
        self.ism=ism
        self.firma=firma
        self.raqami=raqami
        self.staji=staji
    def update_staji(self,s):
        self.staji=s
    def get_info(self):
        print(f'Ismi : {self.ism}\nFirma : {self.firma}\nRaqami : {self.raqami}\nStaji : {self.staji}\n')
class Jurnal:
    def __init__(self,nomi,davriylik,korinishi,nashriyot):
        self.nomi=nomi
        self.davriylik=davriylik
        self.korinishi=korinishi
        self.nashriyot=nashriyot
    def set_nomi(self,s):
        self.nomi=s
    def get_info(self):
        print(f"Nomi : {self.nomi}\nDavriyligi : {self.davriylik}\nKor'inishi : {self.korinishi}\nNashriyot : {self.nashriyot}\n")
class Mahsulot:
    def __init__(self,nomi,narxi,mamlakat):
        self.nomi=nomi
        self.soni=14
        self.narxi=narxi
        self.mamlakat=mamlakat
    def set_narxi(self,s):
        self.narxi+=self.narxi*s/100
    def get_info(self):
        print(f"Nomi : {self.nomi}\nSoni : {self.soni}\nnarxi : {self.narxi}\nMamlakat : {self.mamlakat}\n")
class kivitasiya:
    def __init__(self,raqami,sana,pul_miqdori,manzili):
        self.raqami=raqami
        self.sana=sana
        self.pul_miqdori=pul_miqdori
        self.manzili=manzili
    def set_manzil(self,s):
        self.manzili=s
    def get_info(self):
        print(f"Raqami : {self.raqami}\nSana : {self.sana}\nPul miqdori : {self.pul_miqdori}\nManzil : {self.manzili}\n")
class Tikuvchilik_sexi:
    def __init__(self,ismi,boshliq,ishchi_soni,zavod):
        self.ismi=ismi
        self.boshliq=boshliq
        self.ishchi_soni=ishchi_soni
        self.zavod=zavod
    def set_ishchi_soni(self,s):
        self.ishchi_soni=s
    def get_info(self):
        print(f'ismi : {self.ismi}\nboshliq : {self.boshliq}\nishchilar soni : {self.ishchi_soni}\nzavod : {self.zavod}\n')
class shaxs:
        def __init__(self,ismi,yoshi,jinsi,millati):
            self.ismi=ismi
            self.yoshi=yoshi
            self.jinsi=jinsi
            self.millati=millati
        def set_millat(self,s):
            self.millati=s
        def get_info(self):
            print(f'ismi : {self.ismi}\nyoshi : {self.yoshi}\njinsi : {self.jinsi}\nmillat : {self.millati}\n')
class korabl:
        def __init__(self,ismi,suv_siljishi,turi,yoshi):
            self.ismi=ismi
            self.suv_siljishi=suv_siljishi
            self.turi=turi
            self.yoshi=yoshi
        def set_turi(self,s):
            self.turi=s
        def get_info(self):
            print(f'ismi : {self.ismi}\nsuv siljishi : {self.suv_siljishi}\nturi : {self.turi}\nyoshi : {self.yoshi}\n')
class shahar:
        def __init__(self,nomi,respublikasi,tuman,xuquqiy_holat):
            self.nomi=nomi
            self.respublikasi=respublikasi
            self.tuman=tuman
            self.xuquqiy_holat=xuquqiy_holat
        def set_nomi(self,s):
            self.nomi=s
        def get_info(self):
            print(f'nomi : {self.nomi}\nrespublikasi : {self.respublikasi}\ntuman : {self.tuman}\nxuquqiy holat : {self.xuquqiy_holat}\n')
class tasvir:
        def __init__(self,nomi,tasvirchi,yili,galereya):
            self.nomi=nomi
            self.tasvirchi=tasvirchi
            self.yili=yili
            self.galereya=galereya
        def set_yili(self,s):
            self.yili=s
        def get_info(self):
            print(f'nomi : {self.nomi}\ntasvirchi : {self.tasvirchi}\nyili : {self.yili}\ngalereya : {self.galereya}\n')
class ijarachi:
        def __init__(self,ismi,mamlakat,yoshi,sayohat_maqsadi):
            self.ismi=ismi
            self.mamlakat=mamlakat
            self.yoshi=yoshi
            self.sayohat_maqsadi=sayohat_maqsadi
        def update_yoshi(self):
            self.yoshi=19
        def get_info(self):
            print(f'ismi : {self.ismi}\nmamlakat : {self.mamlakat}\nyoshi : {self.yoshi}\nsayohat_maqsadi : {self.sayohat_maqsadi}\n')
class telefon:
        def __init__(self,abonet_ismi,raqami,manzil,turi):
            self.abonet_ismi=abonet_ismi
            self.raqami=raqami
            self.manzil=manzil
            self.turi=turi
        def set_raqami(self,s):
            self.raqami=s
        def get_info(self):
            print(f'abonet ismi : {self.abonet_ismi}\nraqami : {self.raqami}\nmanzil : {self.manzil}\nturi : {self.turi}\n')
class futbolchi:
        def __init__(self,ismi,yoshi,kim_bolib_oynaydi,gollar_soni):
            self.ismi=ismi
            self.yoshi=yoshi
            self.kim_bolib_oynaydi=kim_bolib_oynaydi
            self.gollar_soni=gollar_soni
        def set_gollar_soni(self,s):
            self.gollar_soni=s
        def get_info(self):
            print(f'ismi : {self.ismi}\nyoshi : {self.yoshi}\nkim_bolib_oynaydi : {self.kim_bolib_oynaydi}\ngollar_soni : {self.gollar_soni}\n')
class disk:
        def __init__(self,nomi,hajmi,narxi,mamlakat):
            self.nomi=nomi
            self.hajmi=hajmi
            self.narxi=narxi
            self.mamlakat=mamlakat
        def set_narxi(self,s):
            self.narxi=s
        def get_info(self):
            print(f'nomi : {self.nomi}\nhajmi : {self.hajmi}\nnarxi : {self.narxi}\nmamlakat : {self.mamlakat}\n')
class ustoz:
        def __init__(self,ismi,yoshi,maktab,sinf):
            self.ismi=ismi
            self.yoshi=yoshi
            self.maktab=maktab
            self.sinf=sinf
        def set_sinf(self,s):
            self.sinf=s
        def get_info(self):
            print(f'ismi : {self.ismi}\nyoshi : {self.yoshi}\nmaktab : {self.maktab}\nsinf : {self.sinf}\n')
class fan:
        def __init__(self,nomi,soat_hajmi,kurs,turi):
            self.nomi=nomi
            self.soat_hajmi=soat_hajmi
            self.kurs=kurs
            self.turi=turi
        def set_kurs(self,s):
            self.kurs=s
        def get_info(self):
            print(f'nomi : {self.nomi}\nsoat_hajmi : {self.soat_hajmi}\nkurs : {self.kurs}\nturi : {self.turi}\n')