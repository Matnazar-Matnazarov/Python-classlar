import mysql.connector
ulanish=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="uquv_markaz"
)
cursor=ulanish.cursor()
cursor.execute("SELECT * FROM uquvchilar")
talabalar=cursor.fetchall()
for i in talabalar:
    print(i)