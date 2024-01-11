class Avtosalon:
    def __init__(self,nomi,narxi) -> None:
        self.nomi=nomi
        self.narxi=narxi
        self.avtolar=[]
    def __repr__(self) -> str:
        return f'Nomi : {self.nomi}\nNarxi : {self.narxi}\n'
    def __call__(self,*s):
        for i in s:
            self.avtolar.append(i)
    def __getitem__(self,index):
        try:
            return self.avtolar[index]
        except IndexError:
            return "Bunday index yo'q"
    def __setitem__(self,index,s):
        try:
            self.avtolar[index]=s
        except IndexError:
            return "Bunday index yo'q 2"
