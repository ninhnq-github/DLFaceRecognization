import numpy as np
import cv2
import numpy as np
import sqlite3
import mysql.connector
import os
def insertOrupdate(id,name):
    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Nmaster2000", database = "nhan_dien_SV")
    query = "SELECT * FROM people WHERE id="+str(id)

    cur = myconn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    
    isRecordExist=0
    for row in records:
        isRecordExist=1
    if(isRecordExist==0):
        query="INSERT INTO people(ID,Name) VALUES("+str(id)+",'"+str(name)+"')"
    else:
        query="UPDATE people SET Name='"+str(name)+"' Where id="+str(id)
    cur.execute(query)
    myconn.commit()
    cur.close()
    myconn.close()

def Get_Image_To_Database(id,name):
    
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    
    cap = cv2.VideoCapture(0)
    #insert to db:
    insertOrupdate(id,name)
    sampleNum=0
    while (True):
        ret, frame = cap.read()
     #   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     #   faces = face_cascade.detectMultiScale(gray)
     #   for (x, y, w, h) in faces:
     #       cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
     #       if not os.path.exists('dataset'):
     #           os.makedirs('dataset')
     #       sampleNum=sampleNum+1
     #       cv2.imwrite('dataset/User.'+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w]) 

     #       roi_gray = gray[y:y + h, x:x + w]
     #       roi_color = frame[y:y + h, x:x + w]

        if not os.path.exists('train_img'):
                os.makedirs('train_img')
        if not os.path.exists('train_img/'+str(id)):
                os.makedirs('train_img/'+str(id))
        sampleNum=sampleNum+1
        cv2.imwrite('train_img/'+str(id)+"/"+str(sampleNum)+".jpg",frame) 
        roi_color = frame;
        cv2.imshow('Chụp ảnh', frame)
        cv2.waitKey(1)
        if(sampleNum>250):
            break
    cap.release()
    cv2.destroyAllWindows()