from  mysql_baza import *
from  excel_class import *
mb=Database()
# kurslar=mb.kurslar_nomi()
# print(kurslar)
# kurs_id=mb.kurs_nomi(5)
# print(kurs_id)
# uqituvchilar=mb.uqituvchilar_fio()
# print(uqituvchilar)
# uqituvchi_qidir=mb.search_uquvchi("bek")
# print(uqituvchi_qidir)
# qatnashgashayotgan_uquvchilar=mb.count_kurs_uquvchilari("Kompyuter grafikasi")
# print(qatnashgashayotgan_uquvchilar)
# tulovlar=mb.sum_tulovlar("2024-01-04")
# print(tulovlar)
# oraliq_tulov=mb.sum_sanalar_tulovi("2024-01-04","2024-01-11")
# print(oraliq_tulov)
# uqituvchi_fani=mb.uqituvchi_kurslari("Mahmudjon","Sodiqov")
# print(uqituvchi_fani)
# uqituvchining_uquvchilari=mb.uqituvchi_uquvchilari("Azizbek",'Xaitboyev')
# print(uqituvchining_uquvchilari)
# uquvchining_uqtuvchilari=mb.uquvchi_uqituvchisi("Dastonbek","Sotliqov")
# print(uquvchining_uqtuvchilari)
# kurs_uquvchilari_=mb.kurs_uquvchilari(9)
# print(kurs_uquvchilari_)
# sanadagi_tulovlar_soni=mb.count_tulovlar("2024-01-04")
# print(sanadagi_tulovlar_soni)
# sum_uqituvchi_tulov_sana=mb.sum_uqituvchi_tulovlari(13,"2024-01-01","2024-01-13")
# print(sum_uqituvchi_tulov_sana)
# uquvchi_tulov=mb.sum_uquvchi_tulovlari(2)
# print(uquvchi_tulov)
# mb.kurs_narxini_oshirish(1,5,10)
# mb.insert_kurslar("C++",400000,"8 oy")
# mb.insert_uquvchilar("Matnazarbek","Matnazarov","2004-07-30","+998918690730")
# mb.insert_uqituvchilar("Fahriddin","Azodov","Fizika","+998905577783")
# mb.insert_tulov("Matnazarbek","Matnazarov",440000,"python asoslari")
# mb.change_dars_vaqti("Janar","Yusupova","15:00:00")
# mb.SqlToTable("kurslar")
mb.TableToSql('uquvchilar','uquvchilar')