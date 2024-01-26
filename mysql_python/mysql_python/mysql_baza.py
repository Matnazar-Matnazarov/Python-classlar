import mysql.connector
import datetime
class Database:
    def __init__(self):
        self.db=self.ulanish()
        self.cursor=self.db.cursor()
    def ulanish(self):
        return mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="uquv_markaz"
                )
    def kurslar_nomi(self):
        sr="SELECT kurs_nomi FROM kurslar"
        return "\n".join(map(str,self.ishlatish(sr,fetchall=True)))
    def kurs_nomi(self,id):
        sq=f"SELECT kurs_nomi FROM kurslar WHERE id={id}"
        return self.ishlatish(sq,fetchone=True)
    def uqituvchilar_fio(self):
        sq="SELECT ism,familiya FROM uqituvchilar"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def search_uquvchi(self,s):
        sq=f"SELECT ism FROM uqituvchilar WHERE ism LIKE '%{s}%'"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def count_kurs_uquvchilari(self,s):
        sq=f"SELECT * FROM uquvchilar WHERE id IN (SELECT uquvchi_id FROM uquvchi_kurslari WHERE kurs_id IN (SELECT id FROM kurslar WHERE kurs_nomi='{s}'))"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def sum_tulovlar(self,sana):
        sq=f"SELECT SUM(tulov) FROM tulovlar WHERE '{sana} 00:00:00'<=vaqti AND vaqti<='{sana} 23:59:59'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def sum_sanalar_tulovi(self,s1,s2):
        sq=f"SELECT SUM(tulov) FROM tulovlar WHERE '{s1} 00:00:00'<=vaqti AND vaqti<='{s2} 23:59:59'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def uqituvchi_kurslari(self,ism,familiyasi):
        sq=f"SELECT kurs_nomi FROM kurslar WHERE id IN (SELECT kurs_id FROM uqituvchi_kurslari WHERE uqituvchi_id IN (SELECT id FROM uqituvchilar WHERE ism='{ism}' AND familiya='{familiyasi}'))"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def uqituvchi_uquvchilari(self,ism,familiya):
        sq=f"SELECT ism,familiya FROM uquvchilar WHERE id IN (SELECT uquvchi_id FROM uquvchi_kurslari WHERE uqituvchi_id IN (SELECT id FROM uqituvchilar WHERE ism='{ism}' AND familiya='{familiya}'))"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def uquvchi_uqituvchisi(self,ism,familiya):
        sq=f"SELECT ism,familiya FROM uqituvchilar WHERE id  IN (SELECT uqituvchi_id FROM uquvchi_kurslari WHERE uquvchi_id IN (SELECT id FROM uquvchilar WHERE ism='{ism}' AND familiya='{familiya}'))"
        return "\n".join(map(str,self.ishlatish(sq,fetchall=True)))
    def kurs_uquvchilari(self,id):
        sq=f"SELECT COUNT(uquvchi_id) FROM uquvchi_kurslari WHERE kurs_id = '{id}'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def count_tulovlar(self,sana):
        sq=f"SELECT COUNT(tulov) FROM tulovlar WHERE '{sana} 00:00:00'<=vaqti AND vaqti<='{sana} 23:59:59'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def sum_uqituvchi_tulovlari(self,id,s1,s2):
        sq=f"SELECT SUM(tulov) FROM tulovlar WHERE uquvchi_id IN (SELECT uquvchi_id FROM uquvchi_kurslari WHERE uqituvchi_id = '{id}') AND '{s1} 00:00:00'<=vaqti AND vaqti<='{s2} 23:59:59'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def sum_uquvchi_tulovlari(self,id):
        sq=f"SELECT SUM(tulov) FROM tulovlar WHERE uquvchi_id='{id}'"
        return "\n".join(map(str,self.ishlatish(sq,fetchone=True)))
    def kurs_narxini_oshirish(self,id1,id2,foiz):
        sq = f"UPDATE kurslar SET narxi=narxi+narxi*{foiz}/100.0 WHERE id BETWEEN '{id1}' AND '{id2}'"
        self.ishlatish(sq,commit=True)
    def insert_kurslar(self,kurs_nomi,narxi,davomiyligi):
        sq=f"INSERT INTO kurslar (kurs_nomi,narxi,davomiyligi) VALUES ('{kurs_nomi}',{narxi},'{davomiyligi}')"
        self.ishlatish(sq,commit=True)
    def insert_uquvchilar(self,ism,familiya,t_sana,tel):
        sq=f"INSERT INTO uquvchilar (ism,familiya,tugulgan_sana,tel_raqam) VALUES ('{ism}','{familiya}','{t_sana}','{tel}')"
        self.ishlatish(sq,commit=True)
    def insert_uqituvchilar(self,ism,familiya,yunalishi,tel):
        sq=f"INSERT INTO uqituvchilar (ism,familiya,yunalishi,tel_raqami) VALUES ('{ism}','{familiya}','{yunalishi}','{tel}')"
        self.ishlatish(sq,commit=True)
    def insert_tulov(self,ism, familiya, tulov, kurs_nomi):
        s1=f"SELECT id FROM uquvchilar WHERE ism='{ism}' AND familiya='{familiya}"
        id=str(self.ishlatish(s1,fetchone=True))
        s2=f"SELECT id FROM kurslar WHERE kurs_nomi='{kurs_nomi}'"
        kurs_id=str(self.ishlatish(s2,fetchone=True))
        vaqti=datetime.datetime.now()
        vaqti=str(vaqti)
        sq=f"INSERT INTO tulovlar (uquvchi_id,tulov,kurs_id,vaqti) VALUES ('{id}',{tulov},'{kurs_id}','{vaqti}')"
        self.ishlatish(sq,commit=True)
    def ishlatish(self,sql,fetchall=False,fetchone=False,commit=False):
        date=None
        if fetchall:
            self.cursor.execute(sql)
            date=self.cursor.fetchall()
        if fetchone:
            self.cursor.execute(sql)
            date=self.cursor.fetchone()
        if commit:
            self.cursor.execute(sql)
            self.db.commit()
        if date:
            return date