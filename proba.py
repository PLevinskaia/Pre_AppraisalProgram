################################################################################
##
## BY: PLEVINSKAYA
## PROJECT MADE WITH: Qt Designer and PyQt5
##
################################################################################

import sys
import sqlite3
from random import randint

import self as self
import ui as ui
from PyQt5 import QtWidgets, QtCore, QtGui, QtSql
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel

## ==> Главное меню
from PyQt5.QtWidgets import QMainWindow

from MainW import Ui_MainW

## ==> Окно "Открыть проекты для просмотра"
from ChildV import Ui_Dialog

## ==> Окно "Открыть проекты для просмотра"
from CreatingW import Ui_MainWindow


db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('DB.db')
db.open()
query=QSqlQuery()
query.exec_('''CREATE TABLE PAP (
      Name_Project TEXT PRIMARY KEY,
      Comments TEXT,
      N INTEGER,
      costs_one REAL,
      costs_N REAL)''')



name=None
comments=None
N=None
tabs=[True,True,True,True,True,True,True,True,True,True,True]
rowid=0




# К Главному меню:
class MainW(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainW()
        self.ui.setupUi(self)

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

    def create_project(self):

        global name
        global comments
        global N
        global tabs

        name = self.ui.lineEdit.text()
        comments = self.ui.lineEdit_2.text()
        N = int(self.ui.spinBox.text())
        tabs[0] = self.ui.checkBox.isChecked()
        tabs[1] = self.ui.checkBox_2.isChecked()
        tabs[2] = self.ui.checkBox_3.isChecked()
        tabs[3] = self.ui.checkBox_4.isChecked()
        tabs[4] = self.ui.checkBox_5.isChecked()
        tabs[5] = self.ui.checkBox_7.isChecked()
        tabs[6] = self.ui.checkBox_9.isChecked()
        tabs[7] = self.ui.checkBox_8.isChecked()
        tabs[8] = self.ui.checkBox_6.isChecked()
        tabs[9] = self.ui.checkBox_11.isChecked()
        tabs[10] = self.ui.checkBox_13.isChecked()

        self.createwin = CreatingW()
        self.createwin.show()



        self.query=QSqlQuery()
        self.query.prepare('''INSERT INTO PAP (Name_Project, Comments, N) VALUES (?, ?, ?)''')
        self.query.bindValue(0,self.ui.lineEdit.text())
        self.query.bindValue(1, self.ui.lineEdit_2.text())
        self.query.bindValue(2, int(self.ui.spinBox.text()))
        self.query.exec_()


# К Окну "Открыть проекты для просмотра":
class ChildV(QtWidgets.QDialog):
    def __init__(self):
        super(ChildV, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)





# К Окну "Открыть проекты для просмотра":
class CreatingW(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText(name)
        self.ui.label_8.setText(comments)

        self.ui.tab.setEnabled(tabs[0])
        self.ui.tab_2.setEnabled(tabs[1])
        self.ui.tab_3.setEnabled(tabs[2])
        self.ui.tab_4.setEnabled(tabs[3])
        self.ui.tab_6.setEnabled(tabs[4])
        self.ui.tab_7.setEnabled(tabs[5])
        self.ui.tab_8.setEnabled(tabs[6])
        self.ui.tab_9.setEnabled(tabs[7])
        self.ui.tab_10.setEnabled(tabs[8])
        self.ui.tab_11.setEnabled(tabs[9])
        self.ui.tab_12.setEnabled(tabs[10])




        self.query = QSqlQuery()
        self.query.exec_(
            '''CREATE TABLE Rubka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                pole_1 INTEGER,
                k1 REAL,
                n INTEGER,
                k2 REAL,
                pole_3 TEXT,
                k3 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model = QSqlTableModel()
        self.model.setQuery(self.query)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.show()


        self.query.exec_(
            '''CREATE TABLE Gibka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                pole_1 INTEGER,
                k1 REAL,
                n INTEGER,
                k2 REAL,
                pole_3 TEXT,
                k3 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Gibka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model = QSqlTableModel()
        self.model.setQuery(self.query)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.ui.tableView_3.setModel(self.model)
        self.ui.tableView_3.show()

        self.query.exec_(
            '''CREATE TABLE PROJECT 
                (NameProject TEXT PRIMARY KEY,
                Rubka REAL,
                Gibka REAL,
                Svarka_toch REAL,
                Svarka_shov REAL,
                Tokarn REAL,
                Proboy REAL,
                Sverlovka REAL,
                Rubka_pravka_set REAL,
                Svarka_toch_set REAL,
                Obtyagka_set REAL,
                Privar_set REAL,
                Podrezka_bolg REAL,
                Rezka_prut REAL,
                Rezka_shpil REAL,
                Sborka_bolt REAL,
                Zachistka_bolg REAL,
                allcosts_one REAL,
                allcosts_N REAL)''')

        self.query.prepare(
            '''INSERT INTO PROJECT 
                (NameProject,
                Rubka,
                Gibka,
                Svarka_toch,
                Svarka_shov,
                Tokarn,
                Proboy,
                Sverlovka,
                Rubka_pravka_set,
                Svarka_toch_set,
                Obtyagka_set,
                Privar_set,
                Podrezka_bolg,
                Rezka_prut,
                Rezka_shpil,
                Sborka_bolt,
                Zachistka_bolg,
                allcosts_one,
                allcosts_N) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, name)
        for i in range(19):
            self.query.bindValue(i + 1, 0)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM PROJECT WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_pj = QSqlTableModel()
        self.model_pj.setQuery(self.query)
        self.model_pj.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_pj.select()
        self.ui.tableView_2.setModel(self.model_pj)
        self.ui.tableView_2.show()

        #кнопки окна Рубка:
        self.ui.pushButton_4.clicked.connect(self.add)
        self.ui.pushButton_5.clicked.connect(self.dell)


        # кнопки окна Гибка:
        self.ui.pushButton_6.clicked.connect(self.add_2)
        self.ui.pushButton_7.clicked.connect(self.dell_2)


    def refresh(self, table, query):

        self.model = QSqlTableModel()
        self.model.setQuery(query)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        table.setModel(self.model)
        table.show()

    # функции окна Рубка:

    def k1_func(self,pole_1):
        k1 = {2: 1.0, 3: 1.05, 4: 1.1, 5: 1.3, 6: 1.5}
        return k1[pole_1]

    def k2_func(self, n):
        if 0 <= float(n) < 100:
            return 1.0
        elif 100 <= float(n) < 1000:
            return 0.8
        else:
            return 0.6

    def k3_func(self, pole_3):
        k3 = {'стандартный': 1.0, 'сложный': 1.2, 'особо сложный': 1.5}
        return k3[pole_3]

    def nxN_func(self,n,N):
        return n*N

    def Sone_func(self, k1, k2, k3, un, n):
        return k1 * k2 * k3 * un * n

    def S_func(self, Se, N):
        return Se * N

    # функции окна Гибка:

    def k1_func2(self,pole_1):
        k1 = {1:1.0, 2: 1.05, 3: 1.1, 4: 1.15, 5: 1.2, 6: 1.25}
        return k1[pole_1]

    def k3_func2(self, pole_3):
        k3 = {'1 гиб на лист': 1.0, '2 гиба на лист': 0.9, '3 гиба на лист': 0.95, '4 гиба на лист': 0.8}
        return k3[pole_3]

    # кнопки-функции окна Рубка:

    def add(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Rubka (ID, NameProject, pole_1, k1, n, k2, pole_3, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, alfavit[randint(0,21)]+str(randint(0,100)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, self.ui.spinBox.text())
        self.query.bindValue(3, self.k1_func(int(self.ui.spinBox.text())))
        self.query.bindValue(4, int(self.ui.spinBox_2.text()))
        self.query.bindValue(5, self.k2_func(int(self.ui.spinBox_2.text())))
        self.query.bindValue(6, self.ui.comboBox.currentText())
        self.query.bindValue(7, self.k3_func(self.ui.comboBox.currentText()))
        self.query.bindValue(8, float(self.ui.spinBox_26.text()))
        self.query.bindValue(9, self.nxN_func(int(self.ui.spinBox_2.text()), N))
        self.query.bindValue(10, self.Sone_func(self.k1_func(int(self.ui.spinBox.text())),
                            self.k2_func(int(self.ui.spinBox_2.text())),
                            self.k3_func(self.ui.comboBox.currentText()),
                            float(self.ui.spinBox_26.text()),
                            int(self.ui.spinBox_2.text())))
        self.query.bindValue(11, self.S_func(
                 self.Sone_func(self.k1_func(int(self.ui.spinBox.text())),
                                self.k2_func(int(self.ui.spinBox_2.text())),
                                self.k3_func(self.ui.comboBox.currentText()),
                                float(self.ui.spinBox_26.text()),
                                int(self.ui.spinBox_2.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView, self.query)


    def dell(self):

        self.rowid=self.model.record(self.ui.tableView.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Rubka WHERE ID = ? ''')
        self.query.addBindValue(self.rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView, self.query)





    # кнопки-функции окна Гибка:

    def add_2(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Gibka (ID, NameProject, pole_1, k1, n, k2, pole_3, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, alfavit[randint(0,21)]+str(randint(0,100)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, self.ui.spinBox_3.text())
        self.query.bindValue(3, self.k1_func2(int(self.ui.spinBox_3.text())))
        self.query.bindValue(4, int(self.ui.spinBox_4.text()))
        self.query.bindValue(5, self.k2_func(int(self.ui.spinBox_4.text())))
        self.query.bindValue(6, self.ui.comboBox_2.currentText())
        self.query.bindValue(7, self.k3_func2(self.ui.comboBox_2.currentText()))
        self.query.bindValue(8, float(self.ui.spinBox_27.text()))
        self.query.bindValue(9, self.nxN_func(int(self.ui.spinBox_3.text()), N))
        self.query.bindValue(10, self.Sone_func(self.k1_func2(int(self.ui.spinBox_3.text())),
                            self.k2_func(int(self.ui.spinBox_4.text())),
                            self.k3_func2(self.ui.comboBox_2.currentText()),
                            float(self.ui.spinBox_27.text()),
                            int(self.ui.spinBox_4.text())))
        self.query.bindValue(11, self.S_func(
                 self.Sone_func(self.k1_func2(int(self.ui.spinBox_3.text())),
                                self.k2_func(int(self.ui.spinBox_4.text())),
                                self.k3_func2(self.ui.comboBox_2.currentText()),
                                float(self.ui.spinBox_27.text()),
                                int(self.ui.spinBox_4.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Gibka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_3, self.query)

    def dell_2(self):

        self.rowid=self.model.record(self.ui.tableView_3.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Gibka WHERE ID = ? ''')
        self.query.addBindValue(self.rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Gibka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_3, self.query)


















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

    def openother(self):
        global otherwin
        otherwin=QtWidgets.QDialog()
        ui=Ui_Dialog()
        ui.setupUi(otherwin)
        otherwin.show()