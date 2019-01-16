import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QAction,QFileDialog,qApp,QFontDialog,QMessageBox
from PyQt5.Qt import QFont,QIcon
from PyQt5 import uic
import os

qtCreator_menu='diary.ui'
Ui_Class_Menu,Qt_Class_menu=uic.loadUiType(qtCreator_menu)

class main_class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_initUI()

    def main_initUI(self):
        self.ui_main=Ui_Class_Menu()
        self.ui_main.setupUi(self)
        self.ui_main.memo_btn.clicked.connect(self.memo)
        self.ui_main.attn_btn.clicked.connect(self.attendance)
        self.ui_main.assign_btn.clicked.connect(self.assignement)
        self.ui_main.to_do.clicked.connect(self.todo)

    def memo(self):
        os.system('textEditor.py')

    def attendance(self):
        os.system('attendance_final.py')

    def assignement(self):
        os.system('assignment.py')

    def todo(self):
        os.system('cal_final.py')


app=QApplication(sys.argv)
win=main_class()
win.show()
sys.exit(app.exec_())
