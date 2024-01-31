from  excel_class import *
def massiv(a,sss="sql_malumot"):
    s=[[i for i in j] for j in a]
    harf=[len(i) for i in (s)]
    alifbo=''.join(map(str,[chr(i) for i in range(ord('A'),ord('Z')+1)][:harf[0]]))
    alifbo_matritsa=[]
    for i in range(len(s)):
        alifbo_matritsa.append([j+str(i+1) for j in alifbo])
    fayl=Excel(f'{sss}.xlsx')
    for i in range(len(alifbo_matritsa)):
        for j in range(len(s[i])):
            fayl.write_cell(alifbo_matritsa[i][j],s[i][j])
    fayl.saqlash(f'{sss}.xlsx')
