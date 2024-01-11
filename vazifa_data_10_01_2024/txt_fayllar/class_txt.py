class Text:
    def __init__(self,nomi) -> None:
        self.nomi=nomi
        self.massivv=[]
        with open(f'{self.nomi}','w',encoding='utf-8') as file:
            pass
    def read_r(self,s):
            r=""
            with open(f'{s}','r',encoding='utf-8') as file:
                b=file.read().splitlines()
                for i in b:
                    r+=i+'\n'
            return r
    def read_text(self):
            b=self.read_r(self.nomi)
            self.massivv=[i for i in b.split('\n')]
            print(b)
    def write_text(self,s):
        with open(f'{self.nomi}','w',encoding='utf-8') as file:
            file.write(f'{s}')
            self.massivv.clear()
        b=self.read_r(self.nomi)
        self.massivv=[i for i in b.split('\n')]
    def add_text(self,satr):
        with open(f'{self.nomi}','a',encoding='utf-8') as file:
            file.write(f'{satr}')
    def first_row(self):
        b=self.read_r(self.nomi)
        print(self.massivv[0])
    def massiv(self):   print(self.massivv)
    def __repr__(self) -> str:
         return str(sum([len(i) for i in self.massivv]))
    def __call__(self,object_file,n=0):
        if n==0:    self.add_text(self.read_r(object_file))
        else:   self.write_text(''.join(map(str,[self.read_r(object_file) if i==n-1 else self.massivv[i]+'\n' for i in range(len(self.massivv))])))
    def __getitem__(self,n):
         try:   return self.massivv[n]
         except Exception as e: return f'{e}'
    def __setitem__(self,index,satr):
        try:
            self.massivv[index]=satr
            self.write_text('\n'.join(map(str,self.massivv)))
        except Exception as e:  print(f'{e}')
    def upper_word(self):
         s='\n'.join(map(str,self.massivv))
         self.write_text(' '.join(map(str,[i.title() for i in s.split(" ")])))
    def del_abzas(self):
         self.write_text(''.join(map(str,self.massivv)))
    def upper_row(self):
         s=self.read_r(self.nomi)
         self.write_text('\n'.join(map(str,[(i[0].title())+i[1:]  for i in list(s.split("\n")) if len(i)!=0])))
    def del_row(self,n):
        s=self.read_r(self.nomi)
        a=[i for i in s.split('\n')]
        try:
            a.pop(n-1)
            self.write_text('\n'.join(map(str,a)))
        except Exception as e:  print(f'{e}')
    def get_row(self,n):
        s=self.read_r(self.nomi)
        try:    print([i for i in s.split('\n')][n])
        except Exception as e:  print(f'{e}')
    def del_rows(self,n,m):
        s=self.read_r(self.nomi)
        a=[i for i in s.split('\n')]
        try:    self.write_text('\n'.join(map(str,a[0:n-1]+a[m-1:])))
        except Exception as e:  print(f'{e}')
    def get_rows(self,n,m):
        s=self.read_r(self.nomi)
        a=[i for i in s.split('\n')]
        try:    print('\n'.join(map(str,a[n:m+1])))
        except Exception as e:  print(f'{e}')
    def new_file(self,n,m):
        s=self.read_r(self.nomi)
        a=[i for i in s.split('\n')]
        try:
            t='\n'.join(map(str,a[n:m+1]))
            with open(f'new_file.txt','a',encoding='utf-8') as file:
                file.write(f'{t}')
        except Exception as e:  print(f'{e}')
    def padding_left(self,n):
        s=self.read_r(self.nomi)
        try:    self.write_text('\n'.join(map(str,[' '*n+i for i in [j for j in s.split('\n')]])))
        except Exception as e:  print(f'{e}')
    def append_file(self,object_file):
        s=self.read_r(self.nomi)
        ss=self.read_r(object_file)
        d='\n'.join(map(str,[i for i in s.split('\n')])).split('\n')
        c='\n'.join(map(str,[i for i in ss.split('\n')])).split('\n')
        self.write_text(''.join(map(str,[f"{d[i]} {c[i]}\n" for i in range(min(len(d),len(c)))]+[(d[i] + '\n') if min(len(d), len(c)) == len(c) else (c[i] + '\n') for i in range(min(len(d),len(c)),max(len(d),len(c)))])))