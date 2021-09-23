from PyQt5 import QtCore, QtGui, QtWidgets
#from FaceRecognier import *
from GetImageToData import *
#from Train_Data import *
from train_main import *
from GetInfor_ui import *
from List import *
from face_recognition import *
import sys
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

class Ui_MainWindow(object):
    def OpenGetInforWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_EnterID()
        self.ui.setupUi(self.window)
        self.window.show()

    def ClickRoll(self):
        idList = []
        Recognize(idList)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_List()
        self.ui.setupUi(self.window, idList)
        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 888)
        MainWindow.setStyleSheet("background-color:black")
        self.widget_2 = QtWidgets.QWidget(MainWindow)
        self.widget_2.setGeometry(QtCore.QRect(10, 620, 511, 261))
        self.widget_2.setStyleSheet("Background-color:#FFFFCC")
        self.widget_2.setObjectName("widget_2")
        self.btnGetID = QtWidgets.QPushButton(self.widget_2)
        self.btnGetID.setGeometry(QtCore.QRect(0, 0, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnGetID.setFont(font)
        self.btnGetID.setStyleSheet("QPushButton {\n"
        "    color: rgb(0,0,0);\n"
        "    background-color: #FFCC66;\n"
        "    border: 0px solid;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #CCFFFF;\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Picture1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGetID.setIcon(icon)
        self.btnGetID.setIconSize(QtCore.QSize(70, 70))
        self.btnGetID.setObjectName("btnGetID")
        self.btnGetID.clicked.connect(self.OpenGetInforWindow)
        self.btnTrain = QtWidgets.QPushButton(self.widget_2)
        self.btnTrain.setGeometry(QtCore.QRect(230, 0, 281, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnTrain.setFont(font)
        self.btnTrain.setStyleSheet("QPushButton {\n"
        "    color: rgb(0,0,0);\n"
        "    background-color:#00FF66;\n"
        "    border: 0px solid;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color:#CCFFFF;\n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Picture2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTrain.setIcon(icon1)
        self.btnTrain.setIconSize(QtCore.QSize(80, 80))
        self.btnTrain.setObjectName("btnTrain")
        self.btnTrain.clicked.connect(train)
 #       self.btnTrain.clicked.connect(TrainData)
        self.btnRC = QtWidgets.QPushButton(self.widget_2)
        self.btnRC.setGeometry(QtCore.QRect(0, 150, 511, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRC.setFont(font)
        self.btnRC.setStyleSheet("QPushButton {\n"
        "    color: rgb(0,0,0);\n"
        "    background-color:#0066CC;\n"
        "    border: 0px solid;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: #CCFFFF;\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("facial_recognition-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRC.setIcon(icon2)
        self.btnRC.setIconSize(QtCore.QSize(70, 70))
        self.btnRC.setObjectName("btnRC")
   #     self.btnRC.clicked.connect(Recognize)
        self.btnRC.clicked.connect(self.ClickRoll)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(10, 10, 511, 601))
        self.widget.setStyleSheet("Background-color:#CCFFFF    ")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 531, 621))
        self.label.setFrameShape(QtWidgets.QFrame.VLine)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Picture3.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Điểm danh"))
        self.btnGetID.setText(_translate("MainWindow", "Get ID"))
        self.btnTrain.setText(_translate("MainWindow", "Machine Training"))
        self.btnRC.setText(_translate("MainWindow", "Rooling Call"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

