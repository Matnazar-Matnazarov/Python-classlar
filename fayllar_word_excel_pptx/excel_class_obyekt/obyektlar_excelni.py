from excel_classlar import *
fayl = Excel('fayl_excell.xlsx')
fayl.add("Matnazar","941-22","Xiva")
fayl.add("Shohjahon","941-22","Xiva")
fayl.add("Valijon","941-22","Bog'ot")
print("Jadval :")
fayl.read_text()
fayl.write_cell('D1', 'user_name')
fayl.add("Siroj","941-22","Gurlan")
fayl.qushish('A1', 'B1', 'E1')
print("\nQushish dan keyingi holat:")
fayl.read_text()
print("\nQidiramiz Xivani :", fayl.search('Xiva'))
print("\nMassiv :", fayl.massiv('A1', 'C3'))
fayl.del_cell('C4')
print("Gurlan o'chirildi")
fayl.read_text()
fayl.saqlash('fayl_excell.xlsx')
print(fayl)