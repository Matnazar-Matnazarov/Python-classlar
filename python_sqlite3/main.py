import sqlite3
from  word_class import Word
class Database_Sqlite:
    def __init__(self, path="sqlite.db"):
        self.path = path
    def ulanish(self):
        return sqlite3.connect(self.path)
    def execute(self, sql: str,malu=None,fetchone=False, fetchall=False, commit=False,malumot=False):
        db = self.ulanish()
        cursor = db.cursor()
        if malumot==False:
            cursor.execute(sql)
        data = None
        if fetchone:
            data = cursor.fetchone()
        elif fetchall:
            data = cursor.fetchall()
        elif commit==True and malumot==True:
            cursor.execute(sql,malu)
            db.commit()
        elif commit:
            db.commit()
        db.close()
        return data
    def create_table(self, table_name, *columns):
        sql0 = ','.join([f'{i[0]} {i[1]}' for i in columns])
        sql = f'CREATE TABLE {table_name} ({sql0})'
        self.execute(sql,commit=True)
    def Sql_To_Txt_Docx(self, table_name):
        malumot = self.execute(f'SELECT * FROM {table_name}', fetchall=True)
        s='\n'.join(map(str,[' '.join(map(str,i)) for i in malumot]))
        with open(f'{table_name}.txt', 'w', encoding='utf-8') as file:
            file.write(f'{s}')
        word_fayl=Word(f'{table_name}.docx')
        word_fayl.add_text(s)
        word_fayl.saqlash(f'{table_name}.docx')
    # def insert_table(self,table_nomi,*s):
    #     sql_ustun_nomlari = f"SHOW COLUMNS FROM {table_nomi}"
    #     mass = self.execute(sql_ustun_nomlari, fetchall=True)
    #     ustun_nomlari = [i[0] for i in mass]
    #     malumot_ustun = {}
    #     h=0
    #     for i in ustun_nomlari:
    #         malumot_ustun[i]=s[h]
    #         h+=1
    #     insert_q = f"INSERT INTO {table_nomi} ({', '.join(table_nomi)}) VALUES ({', '.join(['%s'] * len(ustun_nomlari))})"
    #     self.execute(insert_q, tuple(malumot_ustun.values()), commit=True, malumot=True)
