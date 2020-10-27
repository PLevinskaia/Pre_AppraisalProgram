################################################################################
##
## BY: PLEVINSKAYA
## PROJECT MADE WITH: Qt Designer and PyQt5
##
################################################################################

import sys
import sqlite3
import self as self
import ui as ui
from PyQt5 import QtWidgets, QtCore, QtGui



## ==> Главное меню
from PyQt5.QtWidgets import QMainWindow

from MainW import Ui_MainW

## ==> Окно "Открыть проекты для просмотра"
from ChildV import Ui_Dialog

## ==> Окно "Открыть проекты для просмотра"
from CreatingW import Ui_MainWindow


connect = sqlite3.connect('DB.db')
cursor = connect.cursor()
cursor.execute(
     '''CREATE TABLE IF NOT EXISTS PAP (NameProject text primary key,
      N integer,
      costs_one float,
      costs_N float)''')
connect.commit()

name=None
N=None

# К Главному меню:
class MainW(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainW()
        self.ui.setupUi(self)

       # self.name = self.ui.lineEdit
       # self.comments = self.ui.lineEdit_2
       # self.N = self.ui.spinBox
       # self.to1 = self.ui.checkBox
       # self.to2 = self.ui.checkBox_2

       # self.connect_mainw = sqlite3.connect('DB.db')
       # self.cursor_mainw = self.connect_mainw.cursor()
      #  self.cursor_mainw.execute('''INSERT INTO PAP (NameProject, costs_one) VALUES (?, ?)''',
      #                           (self.name, self.N))
      #  self.connect_mainw.commit()



        # MainW Label

        # Действия, происходящие при активации виджетов Главного меню:

        self.ui.commandLinkButton.clicked.connect(self.openother)
        self.ui.pushButton_2.clicked.connect(self.create_project)






    ## ==> Функции Главного меню:

    def openother(self):
        global otherwin
        otherwin=QtWidgets.QDialog()
        ui=Ui_Dialog()
        ui.setupUi(otherwin)
        otherwin.show()

    def create_project(self): #,name=None,comments=None,N=None,to1=None,to2=None):
        #global createwin

        global name
        global N
        name = self.ui.lineEdit.text()
        print(name, 10000)

        N = int(self.ui.spinBox.text())
        print(N, 1000000)




        self.createwin = CreatingW()
        self.createwin.show()
        #ui = Ui_MainWindow()
        #ui.setupUi(createwin)
        #createwin.show()
       # global createproj
      #  createproj = CreatingW()



        self.connect_mainw = sqlite3.connect('DB.db')
        self.cursor_mainw = self.connect_mainw.cursor()
        self.cursor_mainw.execute('''INSERT INTO PAP (NameProject, N) VALUES (?, ?)''',
                                   (self.ui.lineEdit.text(), int(self.ui.spinBox.text())))
        self.connect_mainw.commit()

        #self.comments = self.ui.lineEdit_2
        #self.N = self.ui.spinBox
        #self.to1 = self.ui.checkBox
        #self.to2 = self.ui.checkBox_2


       # self.ui.label.setText(self.name.text())
        #print(self.to1.text())
        #print(self.to1.isChecked())
       # print(ui.tab.objectName())

        #ui.tab.setEnabled(self.to1.isChecked())




        self.connect = sqlite3.connect('DB.db')
        self.c = self.connect.cursor()
        self.c.execute(
        '''CREATE TABLE IF NOT EXISTS Rubka 
            (NameProject text primary key,
            pole_1 integer,
            k1 float,
            n integer,
            k2 float,
            pole_3 text,
            k3 float,
            Un float,
            nxN float,
            costs_one float,
            costs_N float)''')

        self.c.execute(
        '''CREATE TABLE IF NOT EXISTS Gibka
            (NameProject text primary key,
            pole_1 integer,
            k1 float,
            n integer,
            k2 float,
            pole_3 text,
            k3 float,
            Un float,
            nxN float,
            costs_one float,
            costs_N float)''')

        self.connect.commit()

        #def add(self):  # , pole_1=2, n=1, pole_3='стандартный', Un=0):
            #print('1')

            # self.pole_1 = int(self.ui.spinBox)
            # self.n = self.ui.spinBox_2
            # self.pole_3 = self.ui.comboBox
            # self.Un = self.ui.lineEdit






















      #  self.c.execute('''INSERT INTO Rubka (description_TO, costs_1, costs_N) VALUES (?, ?, ?)''',
      #                 (1, 2, 3))
      #  self.conn.commit()


        print('onnect')





       # ui.tab.setEnabled(1,True)
     #   ui.tab_2.setEnabled(0,False)





# К Окну "Открыть проекты для просмотра":
class ChildV(QtWidgets.QDialog):
    def __init__(self):
        super(ChildV, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    ## ==> Функции Окна "Открыть проекты для просмотра":



# К Окну "Открыть проекты для просмотра":
class CreatingW(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global name
        self.ui.label.setText(name)





        #print(name,N)


        #self.connect_crw1 = sqlite3.connect('DB.db')
       # self.c_cr1 = self.connect_crw1.cursor()
        #self.c_cr1.execute(
         #   '''SELECT * FROM PAP''')

        #print(self.c_cr1.fetchall())


       # self.connect_crw1.commit()



      #  self.show()



        print(333)












    ## ==> Функции Окна "Открыть проекты для просмотра":







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainW()
    window.show()
    sys.exit(app.exec_())



# Для конвертирования .ui-файлов в .py-файлы

# pyuic5 MainW.ui -o MainW.py
# pyuic5 ChildV.ui -o ChildV.py
# pyuic5 CreatingW.ui -o CreatingW.py


#Для того, чтобы открывать .ui-файлы из PyCharm

# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#   <class>Form</class>
#   <widget class="QWidget" name="Form">
#     <property name="geometry">
#       <rect>
#         <x>0</x>
#         <y>0</y>
#         <width>640</width>
#         <height>480</height>
#       </rect>
#     </property>
#     <property name="windowTitle">
#       <string>Form</string>
#     </property>
#   </widget>
# <resources/>
# <connections/>
# </ui>