import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import pymongo

#monogDB Compass Database Connectivity
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["login"]

def home():
    login = secondwindow()
    widget.addWidget(login)
    widget.setCurrentIndex(widget.currentIndex()+1)

def homepage(self):
        mala = Mainwindow()
        widget.addWidget(mala)
        widget.setCurrentIndex(widget.currentIndex() + 1) # 1 is number of time want to press button

def error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Check Username Or Password")
    msg.setWindowTitle("Alert!")
    msg.exec_()

#Login Activity
class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("login.ui",self)         #load Ui file

        #Authentication Logic
        def logincheck():
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            y = mydb.logindatabase.find_one({'username': username, 'password': password})
            if y == None:
                print("Check Username Or Password")
                error()
            else:
                print("Account Login Successful")
                home()

        self.lineEdit.returnPressed.connect(lambda: do_action())
        self.lineEdit_2.returnPressed.connect(lambda: do_action())
        def do_action():
            # getting text from the line edit
            self.pushButton.clicked.connect(logincheck)

#second Window to MainActivity
class secondwindow (QtWidgets.QWidget):
    def __init__(self):
        super(secondwindow, self).__init__()
        loadUi("successpage.ui",self)
        self.pushButton.clicked.connect(homepage)

app=QApplication(sys.argv)
mainwindow=Mainwindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1024)
widget.setFixedHeight(600)
widget.show()
app.exec_()