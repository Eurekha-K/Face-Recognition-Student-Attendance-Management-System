import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
import mysql.connector
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Attendance System')
        self.root.geometry('1500x800')

        # ----------------------------Variables-----------------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()

        self.var_class=StringVar()
        self.var_phone=StringVar()
        self.var_dep=StringVar()

        self.var_mentor=StringVar()
        self.var_roll=StringVar() 
        self.var_course=StringVar() 

        self.var_sem=StringVar()
        self.var_year=IntVar()  
        self.var_email=StringVar()

        self.var_address=StringVar()
        self.var_dob=StringVar()







        self.var_search=StringVar()








        
        
        #title label-----
        title_lbl=Label(self.root,text='Student Management System',font=('times new roman',35,'bold'),bg='Black',fg='White')
        title_lbl.place(x=0,y=0,width=1530,height=100)
        
        
        #main_frame--------
        
        main_frame=Frame(self.root,bd=4)
        main_frame.place(x=10,y=100,width=1500,height=700)

        #Left_frame--------
        
        left_frame=LabelFrame(main_frame,bd=4,font=('times new roman',15,'bold'),text='Student Details')
        left_frame.place(x=100,y=5,width=660,height=638)

        #Right_frame--------
        
        right_frame=LabelFrame(main_frame,bd=4,font=('times new roman',15,'bold'),text='Student Details')
        right_frame.place(x=790,y=5,width=660,height=638)
        
        #Current_frame
        
        current_frame=LabelFrame(left_frame,bd=4,font=('times new roman',12,'bold'),text='Current course Details')
        current_frame.place(x=5,y=30,width=640,height=150)
        
        
        #left_frame=LabelFrame(left_frame,bd=4,font=('times new roman',35,'bold'),text='Student_Details')
        #left_frame.place(x=100,y=10,width=660,height=580)
        
        #Department_Label------------------
        
        
        dept_label=Label(current_frame,font=('times new roman',12,'bold'),text='Department')
        dept_label.grid(row=0,column=0,sticky=W)
        
         
        #Cobobox-----------
        
        combo_box=ttk.Combobox(current_frame,textvariable=self.var_dep,font=('times new roman',12,'bold'),state='readonly')
        combo_box['values']=('Select Department','CSE','Mechanical','EEE','ECE','Chemical','Metallurgical','Civil')
        combo_box.current(0)
        combo_box.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #Course_Label------------------
        
        
        course_label=Label(current_frame,font=('times new roman',12,'bold'),text='Course')
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
         
        #Cobobox-----------
        
        combo_course=ttk.Combobox(current_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),state='readonly')
        combo_course['values']=('Select Course','B.tech','BE')
        combo_course.current(0)
        combo_course.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Semister_Label------------------
        
        
        sem_label=Label(current_frame,font=('times new roman',12,'bold'),text='Semister')
        sem_label.grid(row=1,column=0,padx=10,sticky=W)
        
         
        #Semister-----------
        
        combo_sem=ttk.Combobox(current_frame,textvariable=self.var_sem,font=('times new roman',12,'bold'),state='readonly')
        combo_sem['values']=('Select Semister','SEM-1','SEM-2','SEM-3','SEM-4','SEM-5','SEM-6','SEM-7','SEM-8')
        combo_sem.current(0)
        combo_sem.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
        #Year_Label------------------
        
        
        year_label=Label(current_frame,font=('times new roman',12,'bold'),text='Year')
        year_label.grid(row=1,column=2,padx=10,sticky=W)
        
         
        #Semister-----------
        
        combo_year=ttk.Combobox(current_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),state='readonly')
        combo_year['values']=('Select Semister',2022,2023,2024,2025)
        combo_year.current(0)
        combo_year.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        
        
        
        #Class student info
        
        
        #1.student id------------------------------------------------
        
        class_frame=LabelFrame(left_frame,bd=4,font=('times new roman',12,'bold'),text='Class Student Info')
        class_frame.place(x=5,y=190,width=640,height=400)
        
        id_label=Label(class_frame,font=('times new roman',12,'bold'),text='Student Id')
        id_label.grid(row=0,column=0,padx=10,sticky='W',pady=10)
        
        id_entry=Entry(class_frame,textvariable=self.var_id,font=('times new roman',12,'bold'))
        id_entry.grid(row=0,column=1,padx=10,sticky='W',pady=10)
        
        
         #2.Class ----------------------
        
        
        
        cls_label=Label(class_frame,font=('times new roman',12,'bold'),text='Class')
        cls_label.grid(row=1,column=0,padx=10,sticky='W',pady=10)
        
        cls_entry=Entry(class_frame,textvariable=self.var_class,font=('times new roman',12,'bold'))
        cls_entry.grid(row=1,column=1,padx=10,sticky='W',pady=10)
        
        
         #Gender--------------
        
        
        
        gender_label=Label(class_frame,font=('times new roman',12,'bold'),text='Gender')
        gender_label.grid(row=2,column=0,padx=10,sticky='W',pady=10)
        
        gender_entry=Entry(class_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'))
        gender_entry.grid(row=2,column=1,padx=10,sticky='W',pady=10)
        
         
            
        # Email----------------
        
        
        e_label=Label(class_frame,font=('times new roman',12,'bold'),text='Email')
        e_label.grid(row=3,column=0,padx=10,sticky='W',pady=10)
        
        e_entry=Entry(class_frame,textvariable=self.var_email,font=('times new roman',12,'bold'))
        e_entry.grid(row=3,column=1,padx=10,sticky='W',pady=10)
        
         #Adress----------------------------
        
        
        a_label=Label(class_frame,font=('times new roman',12,'bold'),text='Address')
        a_label.grid(row=4,column=0,padx=10,sticky='W',pady=10)
        
        a_entry=Entry(class_frame,textvariable=self.var_address,font=('times new roman',12,'bold'))
        a_entry.grid(row=4,column=1,padx=10,sticky='W',pady=10)
        
        
       # --------------------------------------------------------------------------------------------------
        
         #Student Name------------------------------------------------
        
        
        s_label=Label(class_frame,font=('times new roman',12,'bold'),text='Student Name')
        s_label.grid(row=0,column=2,padx=10,sticky='W',pady=10)
        
        s_entry=Entry(class_frame,textvariable=self.var_name,font=('times new roman',12,'bold'))
        s_entry.grid(row=0,column=3,padx=10,sticky='W',pady=10)
        
        
         #2.Roll No ----------------------
        
        
        
        r_label=Label(class_frame,font=('times new roman',12,'bold'),text='Roll No')
        r_label.grid(row=1,column=2,padx=10,sticky='W',pady=10)
        
        r_entry=Entry(class_frame,textvariable=self.var_roll,font=('times new roman',12,'bold'))
        r_entry.grid(row=1,column=3,padx=10,sticky='W',pady=10)
        
        
         #DOB--------------
        
        
        
        d_label=Label(class_frame,font=('times new roman',12,'bold'),text='DOB')
        d_label.grid(row=2,column=2,padx=10,sticky='W',pady=10)
        
        d_entry=Entry(class_frame,textvariable=self.var_dob,font=('times new roman',12,'bold'))
        d_entry.grid(row=2,column=3,padx=10,sticky='W',pady=10)
        
         
            
        # PhoneNo---------------
        
        
        p_label=Label(class_frame,font=('times new roman',12,'bold'),text='Phone No')
        p_label.grid(row=3,column=2,padx=10,sticky='W',pady=10)
        
        p_entry=Entry(class_frame,textvariable=self.var_phone,font=('times new roman',12,'bold'))
        p_entry.grid(row=3,column=3,padx=10,sticky='W',pady=10)
        
         #Class Teacher----------------------------
        
        
        t_label=Label(class_frame,font=('times new roman',12,'bold'),text='Mentor')
        t_label.grid(row=4,column=2,padx=10,sticky='W',pady=10)
        
        t_entry=Entry(class_frame,textvariable=self.var_mentor,font=('times new roman',12,'bold'))
        t_entry.grid(row=4,column=3,padx=10,sticky='W',pady=10)
        
        
        #Radio Button--1
        self.var_radio1=StringVar()
        radiob1=ttk.Radiobutton(class_frame,text='Take photo sample',variable=self.var_radio1,value='Yes')
        radiob1.grid(row=6,column=0)
        
        #Radio Button--2
        
        radiob2=ttk.Radiobutton(class_frame,text='No photo sample',variable=self.var_radio1,value='No')
        radiob2.grid(row=6,column=1)
        
        #Button Frame
        
        bframe=Frame(class_frame,bd=2,bg='White')
        bframe.place(x=5,y=260,width=620,height=40)
        
        save_btn=Button(bframe,text='Save',command=self.add_data,font=('times new roman',12,'bold'),width=16)
        save_btn.grid(row=0,column=1)
        
        update_btn=Button(bframe,text='Update',font=('times new roman',12,'bold'),width=16,command=self.update_data)
        update_btn.grid(row=0,column=2)
        
        del_btn=Button(bframe,text='Delete',font=('times new roman',12,'bold'),width=16,command=self.delete_data)
        del_btn.grid(row=0,column=3)
        
        reset_btn=Button(bframe,text='Reset',font=('times new roman',12,'bold'),width=16,command=self.reset_data)
        reset_btn.grid(row=0,column=4)
        
        
        nframe=Frame(class_frame,bd=2,bg='White')
        nframe.place(x=5,y=310,width=620,height=40)
        
        take_photo_btn=Button(nframe,text='Take Photo Sample',command=self.generate_dataset,font=('times new roman',12,'bold'),width=33)
        take_photo_btn.grid(row=0,column=1)
        
        update_photo_btn=Button(nframe,text='Update Photo',font=('times new roman',12,'bold'),width=33)
        update_photo_btn.grid(row=0,column=2)
        
        
        
        # ------------SEARCH FRAME--------------------------------
        search_frame=LabelFrame(right_frame,bd=2,font=('times new roman',12,'bold'),text='Search System')
        search_frame.place(x=5,y=135,width=640,height=70)
        
        search_label=Label(right_frame,bd=2,font=('times new roman',12,'bold'),text='Search By : ')
        search_label.grid(row=0,column=0)
        
        combo_search=ttk.Combobox(search_frame,font=('times new roman',12,'bold'),text='Search')
        combo_search['values']=('Select Semister','Roll No','Phone No')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2,pady=10)

        search_entry=Entry(search_frame,textvariable=self.var_search,font=('times new roman',14,'bold'))
        search_entry.grid(row=0,column=2,padx=3)
        
        
        search_btn=Button(search_frame,text='Search',font=('times new roman',10,'bold'),width=15)
        search_btn.grid(row=0,column=3,padx=3)
        
        show_btn=Button(search_frame,text='Show All',font=('times new roman',10,'bold'),width=15)
        show_btn.grid(row=0,column=4)
        
        
        #-------------Table Frame--------------------------
        
        table_frame=Frame(right_frame,bd=2,bg='white')
        table_frame.place(x=5,y=220,width=640,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','class','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading('dep',text='Department')
        self.student_table.heading('course',text='Course')
        self.student_table.heading('year',text='Year')
        
        self.student_table.heading('sem',text='Semister')
        self.student_table.heading('id',text='Student Id')
        self.student_table.heading('dep',text='Department')
        
        self.student_table.heading('name',text='Name')
        self.student_table.heading('class',text='Class')
        self.student_table.heading('roll',text='Roll No')
        
        self.student_table.heading('dob',text='DOB')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('phone',text='Phone No')
        
        self.student_table.heading('address',text='Address')
        self.student_table.heading('teacher',text='Mentor')
        self.student_table.heading('photo',text='PhotoSampleStatus')
       
        self.student_table['show']='headings'
        
        
        self.student_table.column('dep',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('dep',width=100)
        
        self.student_table.column('name',width=100)
        self.student_table.column('class',width=100)
        self.student_table.column('roll',width=100)
        
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        
        self.student_table.column('address',width=100)
        self.student_table.column('teacher',width=100)
        self.student_table.column('photo',width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function Declarations--------------------------------------------------

    def add_data(self):
        if self.var_dep.get()=='Select Department' or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror('Alert! All fields are required! ')
        else:
            try:
                mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = 'face_recognizer'
                )
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute('CREATE TABLE  IF NOT EXISTS student_information(Dep VARCHAR(20),Course VARCHAR(20),Year VARCHAR(20),Sem VARCHAR(20),Id VARCHAR(20),Name VARCHAR(20),Class VARCHAR(20),Roll VARCHAR(20),Gender VARCHAR(20),Dob VARCHAR(20),Email VARCHAR(20),Phone VARCHAR(20),Address VARCHAR(20),Mentor VARCHAR(20),Photo VARCHAR(20))')
    
                mycursor.execute("insert into student_information values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_class.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_mentor.get(),
                                                                                                        self.var_radio1.get()
                                                                                                          ))
                mydb.commit()
                self.fetch_data()  
                messagebox.showinfo('Success! Student details added. ')
            except Exception as es:
                messagebox.showinfo('Error',f'Due to:{str(es)}')

    #############################################Fetching Data#################################################################

    def fetch_data(self):
        mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = 'face_recognizer'
                )
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("select * from student_information")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                mydb.commit()
            mydb.close()
            
    ####------------------------Get Cursor---------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_mentor.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    ### Update Function###############
    def update_data(self):
        if self.var_dep.get()=='Select Department' or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror('Alert! All fields are required! ',parent=self.root)
        else:
            try:
                upd=messagebox.askyesno('Update','Do you want to update this student details',parent=self.root)
                if upd>0:
                    mydb = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database = 'face_recognizer'
                        )
                    mycursor = mydb.cursor(buffered=True)
                    mycursor.execute('update student_information set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Class=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Mentor=%s,Photo=%s where Id=%s',(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_class.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_mentor.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_id.get()
                                                                                                    ))
                    
                else:
                    if not upd:
                        return
                messagebox.showinfo('Success','Student details updated!',parent=self.root)
                mydb.commit()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                
                
                
        #Delete function ##################################
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror('Alert!Student Id is  required! ',parent=self.root)
        else:
            try:
                dele=messagebox.askyesno('Delete','Do you want to Delete this student details? ',parent=self.root)
                if dele>0:
                    mydb = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database = 'face_recognizer'
                        )
                    mycursor = mydb.cursor(buffered=True) 
                    sql='delete from student_information where Id=%s'
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not dele:
                        return
                messagebox.showinfo('Deleted','Student details deleted!',parent=self.root)
                mydb.commit()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                
                
    # Reset-----------------------------------------------
    def reset_data(self):
        self.var_dep.set('Select Department'),
        self.var_course.set('Select Course'),
        self.var_year.set('Select Year'),
        self.var_sem.set('Select Semister'),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_class.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_mentor.set(""),
        self.var_radio1.set("")
        
        
        
    #Generate data set or Take Photo Samples##################################
    def generate_dataset(self):
        if self.var_dep.get()=='Select Department' or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror('Alert! All fields are required! ',parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = 'face_recognizer'
                    )
                mycursor = mydb.cursor(buffered=True)
                mycursor.execute('select * from student_information')
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id=id+1
                mycursor.execute('update student_information set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Class=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Mentor=%s,Photo=%s where Id=%s',(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_sem.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_class.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_mentor.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_id.get()==id+1
                                                                                                    ))
                mydb.commit()
                self.fetch_data()
                self.reset_data()
                mydb.close()
    
                # Load predefined data on face frontals from Opencv-------------------------------------------------------------
                face_classifier=cv2.CascadeClassifier("C:\\Users\\Welcome\\Desktop\\Attendance\\haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 sacling factor =1.3
                    #Minimum Neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id=img_id+1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="C:\\Users\\Welcome\\Desktop\\Attendance\\Data\\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Cropped face',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result','Generating Dataset completed!!')
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
                

                
                        
                    
                
        

        
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
    