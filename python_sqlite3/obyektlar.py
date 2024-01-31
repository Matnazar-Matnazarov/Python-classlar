from main import Database_Sqlite
obyekt=Database_Sqlite("uquv_markaz.db")
# obyekt.create_table("student", ("id", "INTEGER PRIMARY KEY"), ("ism", "TEXT"), ("familiya", "TEXT"))
# obyekt.insert_table("student",1,"Matnazarbek","Matnazarov")
# obyekt.insert_table("student",2,"Siroj","Sobirov")
# print(obyekt.execute("SELECT * FROM student", fetchall=True))
obyekt.Sql_To_Txt_Docx("student")
