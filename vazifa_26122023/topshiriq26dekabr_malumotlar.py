from topshiriq26dekabr import*
a=ishchi('Ali',12,'5 yil')
b=ishchi('Vali',11,'1 yil')
c=korxona('Konuz',123,'Toshkent')
c.add_ishchi(a)
c.add_ishchi(b)
print(c.get_info())
a=mahsulot('Kompyuter','10000000','Amerika')
b=mahsulot('Telefon','7000000','Germaniya')
c=dukon('Malika','Malika bozor','shahar markazida')
c.add_mahsulotlar(a)
c.add_mahsulotlar(b)
print(c.get_info())
a=tikuvchi('Anora','Anvarovna','yordamchi','1 yil')
b=tikuvchi('Dilnoza','Yoqubova','yordamchi','3 yil')
c=tikuvchiliksexi('Tikuvchilik sexi','derektor',10)
c.add_tikuvchilar(a)
c.add_tikuvchilar(b)
print(c.get_info())
a=shahar('Xiva','yaxshi')
b=shahar('Urganch','yaxshi')
c=viloyat('Xorazm','6.300 kv.km','1.7-2 mln','Uzbekistan')
c.add_shaharlar(a)
c.add_shaharlar(b)
print(c.get_info())
a=futbolchi('Shohjahon',19,'hujumchi',3)
b=futbolchi('Valijon',19,'darvozabon',2)
c=jamoa('tatu',5,0)
c.add_futbolchilar(a)
c.add_futbolchilar(b)
print(c.get_info())
a=ustoz('Shohruh',34,9,'9-E')
b=ustoz('Sanjar',36,9,'5-A')
c=maktab('Orjub',9,'Xiva','yaxshi')
c.add_ustozlar(a)
c.add_ustozlar(b)
print(c.get_info())