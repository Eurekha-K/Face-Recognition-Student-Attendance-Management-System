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
class Train:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Attendance System')
        self.root.geometry('1500x800')



         #title label-----
        title_lbl=Label(self.root,text='Train Dataset',font=('times new roman',35,'bold'),bg='Black',fg='White')
        title_lbl.place(x=0,y=0,width=1530,height=120)

        img1=Image.open("Trainining Bg.jpg")
        img1=img1.resize((1500,600))
        self.photoimg1=ImageTk.PhotoImage(img1)
        Im=Label(root,image=self.photoimg1)
        Im.place(x=0,y=200)
    
        btn1 = Button(self.root,text='Train Data',command=self.train_classifier,cursor='hand2',bg='grey',fg='white',font=('Aerial',28,'bold'))
        btn1.place(x=0,y=120,width=1500,height=80)


    def train_classifier(self):
        data_dir=('Data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



    ####################Training & Save##########################################################
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Training datasets completed !')














if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
    