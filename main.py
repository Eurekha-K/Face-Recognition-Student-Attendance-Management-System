import tkinter
from tkinter import *
from tkinter import ttk
import face_recognition
import cv2
import os
import numpy 
import csv
from PIL import Image,ImageTk
from data_student import student
from train import Train
from face_recognition import Face_Recognition

class facerecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790')
        self.root.configure(bg='black')
        self.root.title('Smart Attendance System')
        #img=Image.open(r"istockphoto-838009174-612x612.jpg")
        #img=img.resize((1500,790))
        #self.photoimg=ImageTk.PhotoImage(img)

        #lb1=Label(self.root,image=self.photoimg)
        #lb1.place(x=0,y=0,width=1500,height=790)

        #student image
        label_=Label(self.root,text='Face Recognition Management System',font=('aerial',50,'bold'))
        label_.place(x=0,y=0,height=120,width=1530)
        

        #-----Student Button


        img1=Image.open(r"femalestudent-1.png")
        img1=img1.resize((220,220))
        self.photoimg1=ImageTk.PhotoImage(img1)

    
        btn1 = Button(self.root,image=self.photoimg1,cursor='hand2',command=self.student_details)
        btn1.place(x=200,y=200,width=220,height=220)

        btn1= Button(root,text="Student Details",bg='grey', fg='white',cursor='hand2',command=self.student_details)
        btn1.place(x=200,y=400,width=220,height=40)

        #--------------Detect Face

        img2=Image.open(r"C:\Users\Welcome\Desktop\Attendance\c621431b20cb2a5f78b1e1cde3b8d35a.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)

    
        btn2 = Button(self.root,image=self.photoimg2,cursor='hand2',command=self.face_data)
        btn2.place(x=500,y=200,width=220,height=220)

        btn2 = Button(root,text="Face Detector",bg='grey', fg='white',cursor='hand2',command=self.face_data)
        btn2.place(x=500,y=400,width=220,height=40)


        #--------------Attendance Face Button

        img3=Image.open(r"shutterstock_1456783511-1-300x300.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)

    
        btn3 = Button(self.root,image=self.photoimg3,cursor='hand2')
        btn3.place(x=800,y=200,width=220,height=220)

        btn3 = Button(root,text="Attendance Face Button",bg='grey', fg='white',cursor='hand2')
        btn3.place(x=800,y=400,width=220,height=40)


         #--------------Help Face Button

        img4=Image.open(r"face-recog-768x511.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

    
        btn4 = Button(self.root,image=self.photoimg4,cursor='hand2')
        btn4.place(x=1100,y=200,width=220,height=220)

        btn4 = Button(root,text="Help Face Button",bg='grey', fg='white',cursor='hand2')
        btn4.place(x=1100,y=400,width=220,height=40)


        
        
       
       
        #--------------Train Data

        img5=Image.open(r"bigstock-Face-Detection-And-Recognition-194513554.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

    
        btn5 = Button(self.root,image=self.photoimg5,cursor='hand2',command=self.train_data)
        btn5.place(x=200,y=500,width=220,height=220)

        btn5 = Button(root,text="Train Data",bg='grey', fg='white',cursor='hand2',command=self.train_data)
        btn5.place(x=200,y=700,width=220,height=40)




         #--------------Photos

        img6=Image.open(r"Photos.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

    
        btn6 = Button(self.root,image=self.photoimg6,cursor='hand2',command=self.open_img)
        btn6.place(x=500,y=500,width=220,height=220)

        btn6 = Button(root,text="Photos",bg='grey', fg='white',cursor='hand2',command=self.open_img)
        btn6.place(x=500,y=700,width=220,height=40)




         #--------------Photos Face Button

        img7=Image.open(r"FacialScanWoman.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

    
        btn7 = Button(self.root,image=self.photoimg7,cursor='hand2')
        btn7.place(x=800,y=500,width=220,height=220)

        btn7= Button(root,text="Developer,command=self.open_img",bg='grey', fg='white',cursor='hand2')
        btn7.place(x=800,y=700,width=220,height=40)



        #--------------Exit

        img8=Image.open(r"Exit exit.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

    
        btn8 = Button(self.root,image=self.photoimg8,cursor='hand2')
        btn8.place(x=1100,y=500,width=220,height=220)

        btn8 = Button(root,text="Exit",bg='grey', fg='white',cursor='hand2')
        btn8.place(x=1100,y=700,width=220,height=40)

    def open_img(self):
        os.startfile("Data")

        ###################################### Functions

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)











if __name__=="__main__":
    root=Tk()
    obj=facerecognition(root)
    root.mainloop()
    
