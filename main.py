################################################################################
##
## BY: PLEVINSKAYA
## PROJECT MADE WITH: Qt Designer and PyQt5
##
################################################################################

import sys

import self as self
import ui as ui
from PyQt5 import QtWidgets, QtCore, QtGui



## ==> Главное меню
from MainW import Ui_MainW

## ==> Окно "Открыть проекты для просмотра"
from ChildV import Ui_Dialog

## ==> Окно "Открыть проекты для просмотра"
from CreatingW import Ui_MainWindow

# К Главному меню:
class MainW(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainW, self).__init__()
        self.ui = Ui_MainW()
        self.ui.setupUi(self)

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

    def create_project(self,name=None,comments=None,N=1,to1=None,to2=None):
        global createwin
        createwin = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(createwin)
        createwin.show()

        self.name = self.ui.lineEdit
        self.comments = self.ui.lineEdit_2.get()
        self.N = self.ui.spinBox.get()


        ui.label.setText(self.name.text())






# К Окну "Открыть проекты для просмотра":
class ChildV(QtWidgets.QDialog):
    def __init__(self):
        super(ChildV, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    ## ==> Функции Окна "Открыть проекты для просмотра":



# К Окну "Открыть проекты для просмотра":
class CreatingW(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreatingW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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