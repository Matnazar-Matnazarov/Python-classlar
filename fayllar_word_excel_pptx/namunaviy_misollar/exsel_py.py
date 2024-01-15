from openpyxl import Workbook
wb=Workbook()
hujjat=wb.active
hujjat['A1']="Bu matn saqlandi"
hujjat['B3']="salom dunyo!"
print(hujjat['A1'].value)
wb.save("date/ex.xlsx")
# o'rganish uchun saytlar
# https://pythonbasics.org/read-excel/
# https://www.geeksforgeeks.org/reading-excel-file-using-python/
# https://www.dataquest.io/blog/reading-excel-file-python/