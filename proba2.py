################################################################################
##
## BY: PLEVINSKAYA
## PROJECT MADE WITH: Qt Designer and PyQt5
##
################################################################################

import sys
import math
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
from OpeningW import Ui_OpeningWindow

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

        self.ui.commandLinkButton.clicked.connect(self.open_project)
        self.ui.pushButton_2.clicked.connect(self.create_project)
        self.ui.pushButton.clicked.connect(self.delete_project)

        self.query = QSqlQuery()
        self.query.exec_('''SELECT * FROM PAP''')
        self.model_PAP = QSqlTableModel()
        self.model_PAP.setQuery(self.query)
        self.model_PAP.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_PAP.select()
        self.ui.tableView.setModel(self.model_PAP)
        self.ui.tableView.show()






    ## ==> Функции Главного меню:

    def open_project(self):

        global name
        global comments
        global N

        name = self.model_PAP.record(self.ui.tableView.currentIndex().row()).value(0)
        comments = self.model_PAP.record(self.ui.tableView.currentIndex().row()).value(1)
        N = int(self.model_PAP.record(self.ui.tableView.currentIndex().row()).value(2))


        self.openwin = OpeningW()
        self.openwin.show()






    def delete_project(self):
        id = self.model_PAP.record(self.ui.tableView.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM PAP WHERE Name_Project = ? ''')
        self.query.addBindValue(id)
        self.query.exec_()
        global name
        name = id
        try:
            self.query.prepare('''DELETE FROM Rubka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Gibka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Svarka_shov WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Svarka_toch WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Proboy WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Sverlovka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Zachistka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Obrabotka_torzov WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Valzovka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Narezka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM Plazma_rezka WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM PROJECT WHERE NameProject = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()

            self.query.prepare('''DELETE FROM PAP WHERE Name_Project = ? ''')
            self.query.addBindValue(name)
            self.query.exec_()
        except:
            pass

        self.query.exec_('''SELECT * FROM PAP''')
        self.model_PAP.setQuery(self.query)
        self.model_PAP.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_PAP.select()
        self.ui.tableView.setModel(self.model_PAP)
        self.ui.tableView.show()


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
class OpeningW(QMainWindow):
    def __init__(self):
        super(OpeningW, self).__init__()
        self.ui = Ui_OpeningWindow()
        self.ui.setupUi(self)

        self.ui.label.setText(name)
        self.ui.label_8.setText(comments)
        self.ui.label_9.setText(str(N))

        self.query = QSqlQuery()
        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
        self.ui.tableView.show()







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
        self.model_Rubka = QSqlTableModel()
        self.model_Rubka.setQuery(self.query)
        self.model_Rubka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Rubka.select()
        self.ui.tableView.setModel(self.model_Rubka)
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
        self.model_Gibka = QSqlTableModel()
        self.model_Gibka.setQuery(self.query)
        self.model_Gibka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Gibka.select()
        self.ui.tableView_3.setModel(self.model_Gibka)
        self.ui.tableView_3.show()

        self.query.exec_(
            '''CREATE TABLE Svarka_shov 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                L REAL,
                type TEXT,
                k1 REAL,
                quality TEXT,
                k2 REAL,
                times TEXT,
                k3 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Svarka_shov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Svarka_shov = QSqlTableModel()
        self.model_Svarka_shov.setQuery(self.query)
        self.model_Svarka_shov.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Svarka_shov.select()
        self.ui.tableView_4.setModel(self.model_Svarka_shov)
        self.ui.tableView_4.show()

        self.query.exec_(
            '''CREATE TABLE Svarka_toch 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Svarka_toch WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Svarka_toch = QSqlTableModel()
        self.model_Svarka_toch.setQuery(self.query)
        self.model_Svarka_toch.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Svarka_toch.select()
        self.ui.tableView_5.setModel(self.model_Svarka_toch)
        self.ui.tableView_5.show()

        self.query.exec_(
            '''CREATE TABLE Proboy 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Proboy WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Proboy = QSqlTableModel()
        self.model_Proboy.setQuery(self.query)
        self.model_Proboy.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Proboy.select()
        self.ui.tableView_6.setModel(self.model_Proboy)
        self.ui.tableView_6.show()

        self.query.exec_(
            '''CREATE TABLE Sverlovka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                tolshina TEXT,
                k1 REAL, 
                diametr TEXT, 
                k2 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Sverlovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Sverlovka = QSqlTableModel()
        self.model_Sverlovka.setQuery(self.query)
        self.model_Sverlovka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Sverlovka.select()
        self.ui.tableView_7.setModel(self.model_Sverlovka)
        self.ui.tableView_7.show()

        self.query.exec_(
            '''CREATE TABLE Zachistka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                L REAL,
                type TEXT,
                k1 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Zachistka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Zachistka = QSqlTableModel()
        self.model_Zachistka.setQuery(self.query)
        self.model_Zachistka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Zachistka.select()
        self.ui.tableView_8.setModel(self.model_Zachistka)
        self.ui.tableView_8.show()

        self.query.exec_(
            '''CREATE TABLE Obrabotka_torzov 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Obrabotka_torzov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Obrabotka_torzov = QSqlTableModel()
        self.model_Obrabotka_torzov.setQuery(self.query)
        self.model_Obrabotka_torzov.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Obrabotka_torzov.select()
        self.ui.tableView_9.setModel(self.model_Obrabotka_torzov)
        self.ui.tableView_9.show()

        self.query.exec_(
            '''CREATE TABLE Valzovka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                tolshina TEXT,
                shirina TEXT, 
                Un REAL,
                n INTEGER,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Valzovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Valzovka = QSqlTableModel()
        self.model_Valzovka.setQuery(self.query)
        self.model_Valzovka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Valzovka.select()
        self.ui.tableView_10.setModel(self.model_Valzovka)
        self.ui.tableView_10.show()

        self.query.exec_(
            '''CREATE TABLE Narezka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                n INTEGER,
                vid TEXT,
                k1 REAL, 
                type TEXT, 
                k2 REAL,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Narezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Narezka = QSqlTableModel()
        self.model_Narezka.setQuery(self.query)
        self.model_Narezka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Narezka.select()
        self.ui.tableView_12.setModel(self.model_Narezka)
        self.ui.tableView_12.show()

        self.query.exec_(
            '''CREATE TABLE Plazma_rezka 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                diametr TEXT,
                k1 REAL,
                n INTEGER,
                Un REAL,
                nxN REAL,
                costs_one REAL,
                costs_N REAL)''')

        self.query.prepare('''SELECT * FROM Plazma_rezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.model_Plazma_rezka = QSqlTableModel()
        self.model_Plazma_rezka.setQuery(self.query)
        self.model_Plazma_rezka.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_Plazma_rezka.select()
        self.ui.tableView_11.setModel(self.model_Plazma_rezka)
        self.ui.tableView_11.show()




        self.query.exec_(
            '''CREATE TABLE PROJECT 
                (ID TEXT PRIMARY KEY,
                NameProject TEXT,
                Rubka REAL,
                Gibka REAL,
                Svarka_shov REAL,
                Svarka_toch REAL,
                Proboy REAL,
                Sverlovka REAL,
                Zachistka REAL,
                Obrabotka_torzov REAL,
                Valzovka REAL,
                Narezka REAL,
                Plazma_rezka REAL,
                None_1 REAL,
                None_2 REAL,
                None_3 REAL,
                None_4 REAL,
                None_5 REAL,
                None_6 REAL,
                allcosts_N REAL)''')

        self.query.prepare(
            '''INSERT INTO PROJECT 
                (ID,
                NameProject,
                Rubka,
                Gibka,
                Svarka_shov,
                Svarka_toch,
                Proboy,
                Sverlovka,
                Zachistka,
                Obrabotka_torzov,
                Valzovka,
                Narezka,
                Plazma_rezka,
                None_1,
                None_2,
                None_3,
                None_4,
                None_5,
                None_6,
                allcosts_N) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.addBindValue('Стоимость изд./эл. '+str(name))
        self.query.bindValue(1, name)
        for i in range(2,21):
            self.query.bindValue(i, 0)
        self.query.exec_()

        self.query.prepare(
            '''INSERT INTO PROJECT 
                (ID,
                NameProject,
                Rubka,
                Gibka,
                Svarka_shov,
                Svarka_toch,
                Proboy,
                Sverlovka,
                Zachistka,
                Obrabotka_torzov,
                Valzovka,
                Narezka,
                Plazma_rezka,
                None_1,
                None_2,
                None_3,
                None_4,
                None_5,
                None_6,
                allcosts_N) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.addBindValue('Стоимость проекта '+str(name))
        self.query.bindValue(1, name)
        for i in range(2, 21):
            self.query.bindValue(i, 0)
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

        # кнопки нижней части окна:
        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_2.clicked.connect(self.clo)
        self.ui.pushButton_3.clicked.connect(self.up)

        # кнопки окна Рубка:
        self.ui.pushButton_4.clicked.connect(self.add)
        self.ui.pushButton_5.clicked.connect(self.dell)

        # кнопки окна Гибка:
        self.ui.pushButton_6.clicked.connect(self.add_2)
        self.ui.pushButton_7.clicked.connect(self.dell_2)

        # кнопки окна Сварка шовная:
        self.ui.pushButton_8.clicked.connect(self.add_3)
        self.ui.pushButton_9.clicked.connect(self.dell_3)

        # кнопки окна Сварка точечная:
        self.ui.pushButton_10.clicked.connect(self.add_4)
        self.ui.pushButton_11.clicked.connect(self.dell_4)

        # кнопки окна Пробой:
        self.ui.pushButton_12.clicked.connect(self.add_5)
        self.ui.pushButton_13.clicked.connect(self.dell_5)

        # кнопки окна Сверловка:
        self.ui.pushButton_14.clicked.connect(self.add_6)
        self.ui.pushButton_15.clicked.connect(self.dell_6)

        # кнопки окна Зачистка:
        self.ui.pushButton_16.clicked.connect(self.add_7)
        self.ui.pushButton_17.clicked.connect(self.dell_7)

        # кнопки окна Обработка торцевых кромок:
        self.ui.pushButton_19.clicked.connect(self.add_8)
        self.ui.pushButton_18.clicked.connect(self.dell_8)

        # кнопки окна Вальцовка:
        self.ui.pushButton_20.clicked.connect(self.add_9)
        self.ui.pushButton_21.clicked.connect(self.dell_9)

        # кнопки окна Нарезка:
        self.ui.pushButton_24.clicked.connect(self.add_10)
        self.ui.pushButton_25.clicked.connect(self.dell_10)

        # кнопки окна Плазменная резка:
        self.ui.pushButton_22.clicked.connect(self.add_11)
        self.ui.pushButton_23.clicked.connect(self.dell_11)


    def refresh(self, table, query, modell):

        modell.setQuery(query)
        modell.select()
        table.setModel(modell)
        table.show()

    # функции нижней части окна:

    def save(self):
        #вызывать функцию кнопки обновить
        self.up()

        self.s_one = 0
        self.s_all = 0
        for i in range(11):
            self.s_one += (self.model_pj.record(0).value(i + 2))
            self.s_all += (self.model_pj.record(1).value(i + 2))

        self.query.prepare('''DELETE FROM PAP WHERE Name_Project = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''INSERT INTO PAP (Name_Project, Comments, N, costs_one, costs_N) VALUES (?, ?, ?, ?, ?)''')
        self.query.bindValue(0, name)
        self.query.bindValue(1, comments)
        self.query.bindValue(2, N)
        self.query.bindValue(3, self.s_one)
        self.query.bindValue(4, self.s_all)
        self.query.exec_()

        self.close()

    def clo(self):

        self.query.prepare('''DELETE FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Gibka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Svarka_shov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Svarka_toch WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Proboy WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Sverlovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Zachistka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Obrabotka_torzov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Valzovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Narezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM Plazma_rezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM PROJECT WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare('''DELETE FROM PAP WHERE Name_Project = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.close()

    def up(self):
        def sum(model, count):
            rows = model.rowCount()
            cost = 0
            for ro in range(rows):
                cost += model.record(ro).value(count)
            return cost

        self.s_one = 0
        self.s_all = 0
        for i in range(11):
            self.s_one += (self.model_pj.record(0).value(i + 2))
            self.s_all += (self.model_pj.record(1).value(i + 2))


        self.query.prepare('''DELETE FROM PROJECT WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()

        self.query.prepare(
            '''INSERT INTO PROJECT 
                (ID,
                NameProject,
                Rubka,
                Gibka,
                Svarka_shov,
                Svarka_toch,
                Proboy,
                Sverlovka,
                Zachistka,
                Obrabotka_torzov,
                Valzovka,
                Narezka,
                Plazma_rezka,
                None_1,
                None_2,
                None_3,
                None_4,
                None_5,
                None_6,
                allcosts_N) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.addBindValue('Стоимость изд./эл. ' + str(name))
        self.query.bindValue(1, name)
        self.query.bindValue(2, sum(self.model_Rubka, 10))
        self.query.bindValue(3, sum(self.model_Gibka, 10))
        self.query.bindValue(4, sum(self.model_Svarka_shov, 12))
        self.query.bindValue(5, sum(self.model_Svarka_toch, 5))
        self.query.bindValue(6, sum(self.model_Proboy, 5))
        self.query.bindValue(7, sum(self.model_Sverlovka, 9))
        self.query.bindValue(8, sum(self.model_Zachistka, 8))
        self.query.bindValue(9, sum(self.model_Obrabotka_torzov, 5))
        self.query.bindValue(10, sum(self.model_Valzovka, 7))
        self.query.bindValue(11, sum(self.model_Narezka, 9))
        self.query.bindValue(12, sum(self.model_Plazma_rezka, 7))
        self.query.bindValue(13, 0)
        self.query.bindValue(14, 0)
        self.query.bindValue(15, 0)
        self.query.bindValue(16, 0)
        self.query.bindValue(17, 0)
        self.query.bindValue(18, 0)
        self.query.bindValue(19, self.s_one)
        self.query.exec_()

        self.query.prepare(
            '''INSERT INTO PROJECT 
                (ID,
                NameProject,
                Rubka,
                Gibka,
                Svarka_shov,
                Svarka_toch,
                Proboy,
                Sverlovka,
                Zachistka,
                Obrabotka_torzov,
                Valzovka,
                Narezka,
                Plazma_rezka,
                None_1,
                None_2,
                None_3,
                None_4,
                None_5,
                None_6,
                allcosts_N) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.addBindValue('Стоимость проекта ' + str(name))
        self.query.bindValue(1, name)
        self.query.bindValue(2, sum(self.model_Rubka, 11))
        self.query.bindValue(3, sum(self.model_Gibka, 11))
        self.query.bindValue(4, sum(self.model_Svarka_shov, 13))
        self.query.bindValue(5, sum(self.model_Svarka_toch, 6))
        self.query.bindValue(6, sum(self.model_Proboy, 6))
        self.query.bindValue(7, sum(self.model_Sverlovka, 10))
        self.query.bindValue(8, sum(self.model_Zachistka, 9))
        self.query.bindValue(9, sum(self.model_Obrabotka_torzov, 6))
        self.query.bindValue(10, sum(self.model_Valzovka, 8))
        self.query.bindValue(11, sum(self.model_Narezka, 10))
        self.query.bindValue(12, sum(self.model_Plazma_rezka, 8))
        self.query.bindValue(13, 0)
        self.query.bindValue(14, 0)
        self.query.bindValue(15, 0)
        self.query.bindValue(16, 0)
        self.query.bindValue(17, 0)
        self.query.bindValue(18, 0)
        self.query.bindValue(19, self.s_all)


        self.query.exec_()

        self.query.prepare('''SELECT * FROM PROJECT WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_2, self.query, self.model_pj)



    # функции окна Рубка:

    def k1_func(self,pole_1):
        k1 = {2: 1.0, 3: 1.05, 4: 1.1, 5: 1.3, 6: 1.5}
        return k1[pole_1]

    def k2_func(self, n):
        if 0 <= float(n*N) < 100:
            return 1.0
        elif 100 <= float(n*N) < 1000:
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

    # функции окна Сварка шовная:

    def type_func(self, type):
        k1 = {'Ручная дуговая': 1.0, 'Аргонодуговая': 1.2, 'Полуавтоматическая': 1.4}
        return k1[type]

    def quality_func(self, quality):
        k2 = {'Стационарные работы': 1.0, 'Стыковка нескольких изделий': 1.2, 'Сборка пространственного каркаса': 1.5}
        return k2[quality]

    def times_func(self, times):
        k3 = {'1 проходка': 1, '2 проходки': 2, '3 проходки': 3, '4 проходки': 4, '5 проходок': 5}
        return k3[times]

    def Sone_func3(self, k1, k2, k3, un, n, L):
        return k1 * k2 * k3 * un * n * L

    # функции окна Сверловка:

    def tolshina_func(self, tolshina):
        k1 = {'до 4 мм': 1.0, 'от 5 до 6 мм': 1.2, 'от 8 до 10 мм': 1.4}
        return k1[tolshina]

    def diametr_func(self, diametr):
        k2 = {'до 13 мм': 1, 'от 13 до 25  мм': 2}
        return k2[diametr]

    # функции окна Зачистка:

    def typez_func(self, type):
        k1 = {'Зачистным кругом': 1.0, 'Лепестковым кругом': 1.2}
        return k1[type]

    # функции окна Вальцовка:

    def n_func(self, shirina, tolshina):
        n = 0
        k2 = {'до 2 мм': 1, '3-4 мм': 2, '5 мм и более': 3}
        if k2[tolshina] == 1:
            n = math.ceil(float(shirina)/200)
        elif k2[tolshina] == 2:
            n = math.ceil(float(shirina)/100)
        elif k2[tolshina] == 3:
            n = math.ceil(float(shirina)/50)
        return n

    # функции окна Нарезка:

    def vid_func(self, vid):
        k1 = {'Болгаркой': 1.5, 'Механической пилой': 1.0, 'Торцовочной пилой': 1.1, 'Плазменная': 1.1}
        return k1[vid]

    def typesec_func(self, type):
        k2 = {'Круг 5 мм': 1.0,
              'Круг 6 мм': 1.44,
              'Круг 8 мм': 2.56,
              'Круг 10 мм': 4.00,
              'Круг 12 мм': 5.76,
              'Квадратный пр. 25х25, 2 мм': 9.01,
              'Квадратный пр. 60х60, 3 мм': 23.27,
              'Квадратный пр. 80х80, 3 мм': 46.29,
              'Прямоугольный пр. 60х40, 2 мм': 19.20,
              'Прямоугольный пр. 80х40, 2 мм': 23.27,
              'Прямоугольный пр. 80х60, 3,5 мм': 46.35,
              'Труба d20, 1,5 мм': 4.44,
              'Труба d22, 2,0 мм': 6.40,
              'Труба d27, 2,5 мм': 9.80,
              'Труба d40, 2,0 мм': 12.16,
              'Труба d76, 1,5 мм': 17.88,
              'Труба d100, 2,0 мм': 31.36,
              'Шпилька М8': 2.82,
              'Шпилька М10': 4.40,
              'Шпилька М12': 6.34,
              'Шпилька М16': 11.26}
        return k2[type]

    # функции окна Нарезка:

    def diametrpl_func(self, diametr):
        k1 = {'до 50 мм': 1.0, 'от 50 до 100 мм': 0.9, 'более 100 мм': 0.9}
        return k1[diametr]









    # кнопки-функции окна Рубка:

    def add(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Rubka (ID, NameProject, pole_1, k1, n, k2, pole_3, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
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
        self.refresh(self.ui.tableView, self.query, self.model_Rubka)

    def dell(self):

        rowid=self.model_Rubka.record(self.ui.tableView.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Rubka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Rubka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView, self.query, self.model_Rubka)

    # кнопки-функции окна Гибка:

    def add_2(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Gibka (ID, NameProject, pole_1, k1, n, k2, pole_3, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
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
        self.refresh(self.ui.tableView_3, self.query, self.model_Gibka)

    def dell_2(self):

        rowid=self.model_Gibka.record(self.ui.tableView_3.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Gibka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Gibka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_3, self.query, self.model_Gibka)

    # кнопки-функции окна Сварка шовная:

    def add_3(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Svarka_shov (ID, NameProject, n, L, type, k1, quality, k2, times, k3, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_5.text()))
        self.query.bindValue(3, float(self.ui.spinBox_13.text()))
        self.query.bindValue(4, self.ui.comboBox_3.currentText())
        self.query.bindValue(5, self.type_func(self.ui.comboBox_3.currentText()))
        self.query.bindValue(6, self.ui.comboBox_4.currentText())
        self.query.bindValue(7, self.quality_func(self.ui.comboBox_4.currentText()))
        self.query.bindValue(8, self.ui.comboBox_7.currentText())
        self.query.bindValue(9, self.times_func(self.ui.comboBox_7.currentText()))
        self.query.bindValue(10, float(self.ui.spinBox_28.text()))
        self.query.bindValue(11, self.nxN_func(int(self.ui.spinBox_5.text()), N))
        self.query.bindValue(12, self.Sone_func3(self.type_func(self.ui.comboBox_3.currentText()),
                                                 self.quality_func(self.ui.comboBox_4.currentText()),
                                                 self.times_func(self.ui.comboBox_7.currentText()),
                                                 float(self.ui.spinBox_28.text()),
                                                 int(self.ui.spinBox_5.text()),
                                                 float(self.ui.spinBox_13.text())))
        self.query.bindValue(13, self.S_func(self.Sone_func3(self.type_func(self.ui.comboBox_3.currentText()),
                                                 self.quality_func(self.ui.comboBox_4.currentText()),
                                                 self.times_func(self.ui.comboBox_7.currentText()),
                                                 float(self.ui.spinBox_28.text()),
                                                 int(self.ui.spinBox_5.text()),
                                                 float(self.ui.spinBox_13.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Svarka_shov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_4, self.query, self.model_Svarka_shov)

    def dell_3(self):

        rowid=self.model_Svarka_shov.record(self.ui.tableView_4.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Svarka_shov WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Svarka_shov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_4, self.query, self.model_Svarka_shov)

    # кнопки-функции окна Сварка точечная:

    def add_4(self):
        alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare(
            '''INSERT INTO Svarka_toch (ID, NameProject, n, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0, 21)] + str(randint(0, 1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_6.text()))
        self.query.bindValue(3, float(self.ui.spinBox_14.text()))
        self.query.bindValue(4, self.nxN_func(int(self.ui.spinBox_6.text()), N))
        self.query.bindValue(5, self.Sone_func(1,1,1,
                                                 float(self.ui.spinBox_14.text()),
                                                 int(self.ui.spinBox_6.text())))
        self.query.bindValue(6, self.S_func(self.Sone_func(1,1,1,
                                                 float(self.ui.spinBox_14.text()),
                                                 int(self.ui.spinBox_6.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Svarka_toch WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_5, self.query, self.model_Svarka_toch)

    def dell_4(self):
        rowid = self.model_Svarka_toch.record(self.ui.tableView_5.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Svarka_toch WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Svarka_toch WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_5, self.query, self.model_Svarka_toch)

    # кнопки-функции окна Пробой:

    def add_5(self):
        alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare(
            '''INSERT INTO Proboy (ID, NameProject, n, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0, 21)] + str(randint(0, 1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_7.text()))
        self.query.bindValue(3, float(self.ui.spinBox_15.text()))
        self.query.bindValue(4, self.nxN_func(int(self.ui.spinBox_7.text()), N))
        self.query.bindValue(5, self.Sone_func(1, 1, 1,
                                               float(self.ui.spinBox_15.text()),
                                               int(self.ui.spinBox_7.text())))
        self.query.bindValue(6, self.S_func(self.Sone_func(1, 1, 1,
                                                           float(self.ui.spinBox_15.text()),
                                                           int(self.ui.spinBox_7.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Proboy WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_6, self.query, self.model_Proboy)

    def dell_5(self):
        rowid = self.model_Proboy.record(self.ui.tableView_6.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Proboy WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Proboy WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_6, self.query, self.model_Proboy)

    # кнопки-функции окна Сверловка:

    def add_6(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Sverlovka (ID, NameProject, n, tolshina, k1, diametr, k2, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_17.text()))
        self.query.bindValue(3, self.ui.comboBox_6.currentText())
        self.query.bindValue(4, self.tolshina_func(self.ui.comboBox_6.currentText()))
        self.query.bindValue(5, self.ui.comboBox_5.currentText())
        self.query.bindValue(6, self.diametr_func(self.ui.comboBox_5.currentText()))
        self.query.bindValue(7, float(self.ui.spinBox_16.text()))
        self.query.bindValue(8, self.nxN_func(int(self.ui.spinBox_17.text()), N))
        self.query.bindValue(9, self.Sone_func(self.tolshina_func(self.ui.comboBox_6.currentText()),
                                                 self.diametr_func(self.ui.comboBox_5.currentText()),
                                                 1,
                                                 float(self.ui.spinBox_16.text()),
                                                 int(self.ui.spinBox_17.text())))
        self.query.bindValue(10, self.S_func(self.Sone_func(self.tolshina_func(self.ui.comboBox_6.currentText()),
                                                 self.diametr_func(self.ui.comboBox_5.currentText()),
                                                 1,
                                                 float(self.ui.spinBox_16.text()),
                                                 int(self.ui.spinBox_17.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Sverlovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_7, self.query, self.model_Sverlovka)

    def dell_6(self):

        rowid=self.model_Sverlovka.record(self.ui.tableView_7.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Sverlovka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Sverlovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_7, self.query, self.model_Sverlovka)

    # кнопки-функции окна Зачистка:

    def add_7(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Zachistka (ID, NameProject, n, L, type, k1, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_8.text()))
        self.query.bindValue(3, float(self.ui.spinBox_19.text()))
        self.query.bindValue(4, self.ui.comboBox_9.currentText())
        self.query.bindValue(5, self.typez_func(self.ui.comboBox_9.currentText()))
        self.query.bindValue(6, float(self.ui.spinBox_18.text()))
        self.query.bindValue(7, self.nxN_func(int(self.ui.spinBox_8.text()), N))
        self.query.bindValue(8, self.Sone_func3(self.typez_func(self.ui.comboBox_9.currentText()),
                                                 1,
                                                 1,
                                                 float(self.ui.spinBox_19.text()),
                                                 int(self.ui.spinBox_8.text()),
                                                 float(self.ui.spinBox_18.text())))
        self.query.bindValue(9, self.S_func(self.Sone_func3(self.typez_func(self.ui.comboBox_9.currentText()),
                                                 1,
                                                 1,
                                                 float(self.ui.spinBox_19.text()),
                                                 int(self.ui.spinBox_8.text()),
                                                 float(self.ui.spinBox_18.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Zachistka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_8, self.query, self.model_Zachistka)

    def dell_7(self):

        rowid=self.model_Zachistka.record(self.ui.tableView_8.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Zachistka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Zachistka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_8, self.query, self.model_Zachistka)

    # кнопки-функции окна Обработка торцевых кромок:

    def add_8(self):
        alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare(
            '''INSERT INTO Obrabotka_torzov (ID, NameProject, n, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0, 21)] + str(randint(0, 1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_10.text()))
        self.query.bindValue(3, float(self.ui.spinBox_20.text()))
        self.query.bindValue(4, self.nxN_func(int(self.ui.spinBox_10.text()), N))
        self.query.bindValue(5, self.Sone_func(1, 1, 1,
                                               float(self.ui.spinBox_20.text()),
                                               int(self.ui.spinBox_10.text())))
        self.query.bindValue(6, self.S_func(self.Sone_func(1, 1, 1,
                                                           float(self.ui.spinBox_20.text()),
                                                           int(self.ui.spinBox_10.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Obrabotka_torzov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_9, self.query, self.model_Obrabotka_torzov)

    def dell_8(self):
        rowid = self.model_Obrabotka_torzov.record(self.ui.tableView_9.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Obrabotka_torzov WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Obrabotka_torzov WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_9, self.query, self.model_Obrabotka_torzov)

    # кнопки-функции окна Вальцовка:

    def add_9(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Valzovka (ID, NameProject, tolshina, shirina, Un, n, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, self.ui.comboBox_8.currentText())
        self.query.bindValue(3, float(self.ui.spinBox_22.text()))
        self.query.bindValue(4, float(self.ui.spinBox_21.text()))
        self.query.bindValue(5, self.n_func(self.ui.spinBox_22.text(), self.ui.comboBox_8.currentText()))
        self.query.bindValue(6, self.nxN_func(self.n_func(float(self.ui.spinBox_22.text()), self.ui.comboBox_8.currentText()), N))
        self.query.bindValue(7, self.Sone_func(1,
                                               1,
                                               1,
                                               float(self.ui.spinBox_21.text()),
                                               self.n_func(self.ui.spinBox_22.text(), self.ui.comboBox_8.currentText())))
        self.query.bindValue(8, self.S_func(self.Sone_func(1,
                                               1,
                                               1,
                                               float(self.ui.spinBox_21.text()),
                                               self.n_func(self.ui.spinBox_22.text(), self.ui.comboBox_8.currentText())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Valzovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_10, self.query, self.model_Valzovka)

    def dell_9(self):

        rowid=self.model_Valzovka.record(self.ui.tableView_10.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Valzovka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Valzovka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_10, self.query, self.model_Valzovka)

    # кнопки-функции окна Нарезка:

    def add_10(self):

        alfavit='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare('''INSERT INTO Narezka (ID, NameProject, n, vid, k1, type, k2, Un, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0,21)]+str(randint(0,1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_11.text()))
        self.query.bindValue(3, self.ui.comboBox_14.currentText())
        self.query.bindValue(4, self.vid_func(self.ui.comboBox_14.currentText()))
        self.query.bindValue(5, self.ui.comboBox_11.currentText())
        self.query.bindValue(6, self.typesec_func(self.ui.comboBox_11.currentText()))
        self.query.bindValue(7, float(self.ui.spinBox_25.text()))
        self.query.bindValue(8, self.nxN_func(int(self.ui.spinBox_11.text()), N))
        self.query.bindValue(9, self.Sone_func(self.vid_func(self.ui.comboBox_14.currentText()),
                                                 self.typesec_func(self.ui.comboBox_11.currentText()),
                                                 1,
                                                 float(self.ui.spinBox_25.text()),
                                                 int(self.ui.spinBox_11.text())))
        self.query.bindValue(10, self.S_func(self.Sone_func(self.vid_func(self.ui.comboBox_14.currentText()),
                                                 self.typesec_func(self.ui.comboBox_11.currentText()),
                                                 1,
                                                 float(self.ui.spinBox_25.text()),
                                                 int(self.ui.spinBox_11.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Narezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_12, self.query, self.model_Narezka)

    def dell_10(self):

        rowid=self.model_Narezka.record(self.ui.tableView_12.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Narezka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Narezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_12, self.query, self.model_Narezka)

    # кнопки-функции окна Плазменная резка:

    def add_11(self):
        alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.query.prepare(
            '''INSERT INTO Plazma_rezka (ID, NameProject, n, Un, diametr, k1, nxN, costs_one, costs_N) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.query.bindValue(0, str(name)+alfavit[randint(0, 21)] + str(randint(0, 1000000)))
        self.query.bindValue(1, name)
        self.query.bindValue(2, int(self.ui.spinBox_23.text()))
        self.query.bindValue(3, float(self.ui.spinBox_24.text()))
        self.query.bindValue(4, self.ui.comboBox_12.currentText())
        self.query.bindValue(5, self.diametrpl_func(self.ui.comboBox_12.currentText()))
        self.query.bindValue(6, self.nxN_func(int(self.ui.spinBox_23.text()), N))
        self.query.bindValue(7, self.Sone_func(self.diametrpl_func(self.ui.comboBox_12.currentText()), 1, 1,
                                               float(self.ui.spinBox_24.text()),
                                               int(self.ui.spinBox_23.text())))
        self.query.bindValue(8, self.S_func(self.Sone_func(self.diametrpl_func(self.ui.comboBox_12.currentText()), 1, 1,
                                               float(self.ui.spinBox_24.text()),
                                               int(self.ui.spinBox_23.text())), N))

        self.query.exec_()

        self.query.prepare('''SELECT * FROM Plazma_rezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_11, self.query, self.model_Plazma_rezka)

    def dell_11(self):
        rowid = self.model_Plazma_rezka.record(self.ui.tableView_11.currentIndex().row()).value(0)
        self.query.prepare('''DELETE FROM Plazma_rezka WHERE ID = ? ''')
        self.query.addBindValue(rowid)
        self.query.exec_()

        self.query.prepare('''SELECT * FROM Plazma_rezka WHERE NameProject = ? ''')
        self.query.addBindValue(name)
        self.query.exec_()
        self.refresh(self.ui.tableView_11, self.query, self.model_Plazma_rezka)


















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
# pyuic5 OpeningW.ui -o OpeningW.py


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