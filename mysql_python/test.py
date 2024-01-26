import MySQLdb
class Database:
    def __init__(self):
        self.db=self.ulanish()
        self.cursor=self.db.cursor()
    def ulanish(self):
        return MySQLdb.connect(
                host="localhost",
                user="root",
                password="root",
                database="uquv_markaz"
                )
    def kurs_narxini_oshirish(self,id1,id2,foiz):
        sq=f"UPDATE kurslar SET narxi=narxi+narxi*{foiz}/100.0 WHERE id BETWEEN '{id1}' AND '{id2}'"
        self.ishlatish(sq,commit=True)
        # self.cursor.execute(sq)
        # self.db.commit()
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
mb=Database()
mb.kurs_narxini_oshirish(1,5,10)