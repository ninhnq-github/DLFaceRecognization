from PyQt5 import QtCore, QtGui, QtWidgets
from GetImageToData import *
class Ui_EnterID(object):
    def setupUi(self, EnterID):
        def ClickOK(se):
            Get_Image_To_Database(self.textEdit.toPlainText(),self.textEdit_2.toPlainText())
         
            print(1)
        def ClickCancel(self):
            print(2)
        EnterID.setObjectName("EnterID")
        EnterID.resize(400, 203)
        EnterID.setStyleSheet("Background-color:#222222")
        self.gbID = QtWidgets.QGroupBox(EnterID)
        self.gbID.setGeometry(QtCore.QRect(30, 10, 341, 131))
        self.gbID.setStyleSheet("color:white")
        self.gbID.setObjectName("gbID")
        self.textEdit = QtWidgets.QTextEdit(self.gbID)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 81, 31))
        self.textEdit.setStyleSheet("background-color:white; color: black")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.gbID)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 80, 231, 31))
        self.textEdit_2.setStyleSheet("background-color:white; color: black")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.gbID)
        self.label.setGeometry(QtCore.QRect(110, 50, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.gbID)
        self.label_2.setGeometry(QtCore.QRect(260, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.btnRC = QtWidgets.QPushButton(EnterID)
        self.btnRC.setGeometry(QtCore.QRect(100, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRC.setFont(font)
        self.btnRC.setStyleSheet("QPushButton {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color:#777777;\n"
            "    border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(85, 170, 255);\n"
            "}")
        self.btnRC.setObjectName("btnRC")
        self.btnRC.clicked.connect(ClickOK)
        
        self.btnRC_2 = QtWidgets.QPushButton(EnterID)
        self.btnRC_2.setGeometry(QtCore.QRect(240, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRC_2.setFont(font)
        self.btnRC_2.setStyleSheet("QPushButton {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background-color:#777777;\n"
            "    border: 0px solid;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: rgb(85, 170, 255);\n"
            "}")
        self.btnRC_2.setObjectName("btnRC_2")
        self.btnRC_2.clicked.connect(ClickCancel)
        


        self.retranslateUi(EnterID)
        QtCore.QMetaObject.connectSlotsByName(EnterID)

    def retranslateUi(self, EnterID):
        _translate = QtCore.QCoreApplication.translate
        EnterID.setWindowTitle(_translate("EnterID", "Information"))
        self.gbID.setTitle(_translate("EnterID", "Enter Information"))
        self.label.setText(_translate("EnterID", "(ID)"))
        self.label_2.setText(_translate("EnterID", "(Name)"))
        self.btnRC.setText(_translate("EnterID", "OK"))
        self.btnRC_2.setText(_translate("EnterID", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterID = QtWidgets.QDialog()
    ui = Ui_EnterID()
    ui.setupUi(EnterID)
    EnterID.show()
    sys.exit(app.exec_())
