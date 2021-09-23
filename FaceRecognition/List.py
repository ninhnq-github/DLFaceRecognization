# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from datetime import datetime
import pandas as pd
import os


def GetProfile(id):
    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Nmaster2000", database = "nhan_dien_sv")
    query = "SELECT * FROM people WHERE id="+str(id)
    cur = myconn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    
    profile=None
    for row in records:
        profile=row

    cur.close()
    myconn.close()
    return profile

def Path():
    now = datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    
    today = day + '-' + month + '-' + year

    path = 'attendance' + '\\' + today + '.xlsx'

    return path

def AttendanceList(idList):
    path = Path()

    #file_object = open(path, mode = 'a+')
    #file_object.seek(0)
    #data = file_object.readlines()
    #file_object.close()
    
    idListText=[]
    if ( os.path.isfile(path)):
        df = pd.read_excel(path)
        data=df.to_dict(orient='record')

        for i in data:
            idListText.append(i['MSSV'])
    #        idListText.append(int(i[0:8]))

    for id in idList:
        if(id not in idListText):
            idListText.append(id)
            idListText.sort()

    return idListText

def AttendanceWrite(idList):
    path = Path()
    
    #file_object = open(path ,mode='w')
    #for id in idList:
    #    file_object.write(str(id) + " - " + GetProfile(id)[1]+'\n')
    #file_object.close();

    ########
    data = {'MSSV':[],'HoVaTen':[]}

    for id in idList:
        data['MSSV'].append(id)
        data['HoVaTen'].append(GetProfile(id)[1])

    df = pd.DataFrame(data)

    df.to_excel(path, sheet_name='States', index=False)



class Ui_List(object):
    def setupUi(self, List, idList):
        List.setObjectName("List")
        List.resize(589, 490)
        List.setStyleSheet("background-color:#111111")
        self.centralwidget = QtWidgets.QWidget(List)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 121, 401))
        self.frame.setStyleSheet("Background-color:#222222")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(-10, 20, 151, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Picture4.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 80, 441, 401))
        self.widget.setStyleSheet("Background-color:#222222")
        self.widget.setObjectName("widget")
        self.lstwtID = QtWidgets.QListWidget(self.widget)
        self.lstwtID.setGeometry(QtCore.QRect(10, 20, 421, 371))
        idList.sort()
        for i in range(0, len(idList)):
            self.lstwtID.addItem(str(idList[i]) + " - " + GetProfile(idList[i])[1])

        idList = AttendanceList(idList)

        AttendanceWrite(idList)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.lstwtID.setFont(font)
        self.lstwtID.setStyleSheet("background:white")
        self.lstwtID.setViewMode(QtWidgets.QListView.ListMode)
        self.lstwtID.setModelColumn(0)
        self.lstwtID.setObjectName("lstwtID")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 571, 61))
        self.widget_2.setStyleSheet("Background-color:#222222")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        List.setCentralWidget(self.centralwidget)

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        _translate = QtCore.QCoreApplication.translate
        List.setWindowTitle(_translate("List", "Danh sách"))
        self.label_3.setText(_translate("List", "LIST OF STUDENTS:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    List = QtWidgets.QMainWindow()
    ui = Ui_List()
    ui.setupUi(List)
    List.show()
    sys.exit(app.exec_())

