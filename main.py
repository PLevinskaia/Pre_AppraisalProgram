from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())


# pyuic5 MainW.ui -o MainW.py
# pyuic5 ChildV.ui -o ChildV.py