import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5 import uic
import os

qtCreator='login.ui'
Ui_MainWindow,qt_BaseClass=uic.loadUiType(qtCreator)

class login_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_initUI()

    def login_initUI(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.yes_btn.clicked.connect(self.yes)
        self.ui.no_btn.clicked.connect(self.no)

    def no(self):
        os.system('index.py')
    def yes(self):
        os.system('subject.py')
        checkbox=QCheckBox()
        checkbox.setText('Data saved properly')
        self.ui.fLayout.addWidget(checkbox)
        checkbox.stateChanged.connect(self.dataSaved)

    def dataSaved(self):
        print('yeah')
        os.system('index.py')


app=QApplication(sys.argv)
win=login_form()
win.show()
sys.exit(app.exec_())