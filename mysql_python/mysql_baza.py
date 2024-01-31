import mysql.connector
import pandas as pd
from  main import *
import datetime
from excel_class import *
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
        # s=""
        # for i in self.ishlatish(sr,fetchall=True):
        #     s+=i[0]+'\n'
        return "\n".join(map(str,self.ishlatish(sr,fetchall=True)))
        # return  s
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
    def fio(self,ism,familiya):
        s1 = f"SELECT id FROM uquvchilar WHERE ism='{ism}' AND familiya='{familiya}'"
        return self.ishlatish(s1, fetchone=True)
    def uqituvchi_fio(self,ism,familiya):
        s1 = f"SELECT id FROM uqituvchilar WHERE ism='{ism}' AND familiya='{familiya}'"
        return self.ishlatish(s1, fetchone=True)
    def kurs_id(self,kurs_nomi):
        s2=f"SELECT id FROM kurslar WHERE kurs_nomi='{kurs_nomi}'"
        return self.ishlatish(s2,fetchone=True)
    def insert_tulov(self,ism, familiya, tulov, kurs_nomi):
        id=self.fio(ism,familiya)
        kurs_id=self.kurs_id(kurs_nomi)
        vaqti=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sq=f"INSERT INTO tulovlar (uquvchi_id,tulov,kurs_id,vaqti) VALUES ({id[0]},{tulov},{kurs_id[0]},'{vaqti}')"
        self.ishlatish(sq,commit=True)
    def change_dars_vaqti(self,ism, familiya, new_vaqt):
        s1=self.uqituvchi_fio(ism,familiya)
        sq=f"UPDATE uqituvchi_kurslari SET vaqti='{new_vaqt}' WHERE uqituvchi_id={s1[0]}"
        self.ishlatish(sq,commit=True)
    def SqlToTable(self,table_nomi):
        sql = f"SELECT * FROM {table_nomi}"
        malumot=self.ishlatish(sql,fetchall=True)
        # massiv(malumot,table_nomi)
        sql_ustun_nomlari=f"SHOW COLUMNS FROM {table_nomi}"
        ustun_nomlari=self.ishlatish(sql_ustun_nomlari,fetchall=True)
        mass=[i[0] for i in ustun_nomlari]
        fayl=Excel()
        fayl.add(malumot,table_nomi,mass)
        fayl.saqlash(table_nomi)
    def TableToSql(self,fayl_nomi,sql_table_name):
        sql_ustun_nomlari = f"SHOW COLUMNS FROM {sql_table_name}"
        mass = self.ishlatish(sql_ustun_nomlari, fetchall=True)
        ustun_nomlari = [i[0] for i in mass]
        fayl=Excel(f'{fayl_nomi}.xlsx',"Sheet1")
        matrix=fayl.matrix()
        # print(matrix)
        for j in matrix:
            malumot_ustun = {}
            h=0
            for i in ustun_nomlari:
                malumot_ustun[i] = j[h]
                h+=1
            insert_q = f"INSERT INTO {sql_table_name} ({', '.join(ustun_nomlari)}) VALUES ({', '.join(['%s'] * len(ustun_nomlari))})"
            self.ishlatish(insert_q,tuple(malumot_ustun.values()),commit=True,malumot_bor=True)
    def ishlatish(self,sql,malumot=None,malumot_bor=False,fetchall=False,fetchone=False,commit=False):
        date=None
        if fetchall:
            self.cursor.execute(sql)
            date=self.cursor.fetchall()
        if fetchone:
            self.cursor.execute(sql)
            date=self.cursor.fetchone()
        if commit:
            if malumot_bor:
                self.cursor.execute(sql,malumot)
                self.db.commit()
            else:
                self.cursor.execute(sql)
                self.db.commit()
        if date:
            return date

