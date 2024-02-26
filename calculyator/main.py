from  PyQt5 import QtWidgets
from  PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5 import  uic
import  sys
from math import *
class asosiy(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/betlash.ui",self)
        self.qiymat=0
        self.satr=""
        self.pushButton_2.clicked.connect(self.button_clear)
        if '=' not in str(self.lineEdit.text()):
            self.pushButton_10.clicked.connect(self.bir)
            self.pushButton_11.clicked.connect(self.ikki)
            self.pushButton_12.clicked.connect(self.uch)
            self.pushButton_14.clicked.connect(self.besh)
            self.pushButton_13.clicked.connect(self.turt)
            self.pushButton_16.clicked.connect(self.yetti)
            self.pushButton_17.clicked.connect(self.sakkiz)
            self.pushButton_15.clicked.connect(self.olti)
            self.pushButton_18.clicked.connect(self.tuqqiz)
            self.pushButton_19.clicked.connect(self.nul)
            self.pushButton_4.clicked.connect(self.kasr)
            self.pushButton_6.clicked.connect(self.kupaytirish)
            self.pushButton_20.clicked.connect(self.nuqta)
            self.pushButton_3.clicked.connect(self.pilus)
            self.pushButton_5.clicked.connect(self.minus)
            self.pushButton.clicked.connect(self.asosiy)
        else:
            self.button_clear()
            self.satr=""
    def bir(self):
        self.satr+=str(1)
        self.yuklash()
    def nul(self):
        self.satr+=str(0)
        self.yuklash()

    def nuqta(self):
        self.satr +="."
        self.yuklash()
    def ikki(self):
        self.satr+=str(2)
        self.yuklash()
    def uch(self):
        self.satr+=str(3)
        self.yuklash()
    def turt(self):
        self.satr+=str(4)
        self.yuklash()
    def besh(self):
        self.satr+=str(5)
        self.yuklash()
    def olti(self):
        self.satr+=str(6)
        self.yuklash()
    def yetti(self):
        self.satr+=str(7)
        self.yuklash()
    def sakkiz(self):
        self.satr+=str(8)
        self.yuklash()
    def tuqqiz(self):
        self.satr+=str(9)
        self.yuklash()
    def yuklash(self):
        self.lineEdit.setText(f"{self.satr}")
    def pilus(self):
        self.satr+='+'
        self.yuklash()
    def minus(self):
        self.satr+='-'
        self.yuklash()
    def kupaytirish(self):
        self.satr+='*'
        self.yuklash()
    def kasr(self):
        self.satr+='/'
        self.yuklash()
    def button_clear(self):
        self.satr=''
        self.yuklash()
    def asosiy(self):
        try:
            javob=eval(str(self.lineEdit.text()))
            javobb='='+str(javob)
            self.satr+=javobb
            self.yuklash()
        except:
            self.button_clear()
            self.satr=""
            pass
if __name__=="__main__":
    app=QApplication([])
    obj=asosiy()
    obj.show()
    sys.exit(app.exec_())