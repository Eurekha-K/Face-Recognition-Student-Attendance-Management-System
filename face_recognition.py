import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
from cv2 import *
import mysql.connector
from tkinter import messagebox
import numpy as np
import numpy
from train import Train

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.title('Face Detector')
        self.root.geometry('1500x800')



        title_lb=Label(self.root,text='Face Recognition',font=('times new roman',35,'bold'),bg='Black',fg='green')
        title_lb.place(x=0,y=0,width=1530,height=120)

        img1_=Image.open("Trainining Bg.jpg")
        img1_=img1_.resize((1500,600))
        self.photoimg1_=ImageTk.PhotoImage(img1_)
        Im_=Label(root,image=self.photoimg1_)
        Im_.place(x=0,y=200)
    
        bt_1 = Button(self.root,text='Face Detector',cursor='hand2',bg='grey',fg='white',font=('Aerial',28,'bold'),command=self.face_recog)
        bt_1.place(x=0,y=120,width=1500,height=80)


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = 'face_recognizer'
                    )
                mycursor = mydb.cursor(buffered=True)

                mycursor.execute('select Name from student_information where Id='+str(id))
                m=mycursor.fetchone()
                m='+'.join(m)


                
                mycursor.execute('select Roll from student_information where Id='+str(id))
                n=mycursor.fetchone()
                n='+'.join(n)

                
                mycursor.execute('select Dep from student_information where Id='+str(id))
                i=mycursor.fetchone()
                i='+'.join(i)

                if confidence>77:
                    cv2.putText(img,f"Name:{m}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dep:{i}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),'face',clf)
            return img
        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome to Face Recognition',img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
    