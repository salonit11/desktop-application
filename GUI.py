from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter"
    )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        #cursor is to retrieve data, one row at a time, from a result set
        #makes it possible to define a result set (a set of data rows) and perform complex logic on a row
        #by row basis.
        
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        #.delete("start","end")
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        #display message
        msg.showinfo('Insert Status','Data inserted successfully')


def search_data():
    #clear textboxes
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    
    if e_id.get=="":
        msg.showinfo("Search Status","Id is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
            #if data is changing then only commit is used
        else:
            msg.showinfo("Search Status","Id not found")
            

def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="update student set fname=%s, lname=%s, email=%s, mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        msg.showinfo('Update Status','Data updated successfully')

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id is mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()

        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()

        #clear textboxes
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')

        msg.showinfo("Delete Status","Data deleted successfully")

def display_data():
    if e_tick.get()=="yes":
        conn=create_conn()
        cursor=conn.cursor()
        
        query="select * from student"
        cursor.execute(query)
        rows=cursor.fetchall()
        conn.close()
    
        if rows:
            id_=Label(root,text='ID',font=("Arial",15,'bold')).grid(row=12,column=0)
            fname=Label(root,text='Fname',font=("Arial",15,'bold')).grid(row=12,column=1)
            lname=Label(root,text='Lname',font=("Arial",15,'bold')).grid(row=12,column=2)
            Email=Label(root,text='Email',font=("Arial",15,'bold')).grid(row=12,column=3)
            mobile=Label(root,text='Mobile',font=("Arial",15,'bold')).grid(row=12,column=4)
            
            for i in range(len(rows)):
                for j in range(5):
                                 
                    e = Label(root,text=rows[i][j],font=('Arial',15))

                    e.grid(row=i+12, column=j)
        else:
            msg.showinfo("Display Status","No data found")

    
root=Tk()
root.geometry("1000x350")
root.title("Desktop Application")
root.resizable(width=False,height=True)

title=Label(root,text="Welcome to Desktop Application",font=("Arial",20)).grid(row=0,column=2)

l_id=Label(root,text='ID',font=("Arial",15)).grid(row=4,column=0)

l_fname=Label(root,text='First Name',font=("Arial",15)).grid(row=4,column=2)

l_lname=Label(root,text='Last Name',font=("Arial",15)).grid(row=5,column=0)

l_email=Label(root,text='Email',font=("Arial",15)).grid(row=5,column=2)

l_mobile=Label(root,text='Mobile',font=("Arial",15)).grid(row=7,column=0)

l_display=Label(root,text='Type yes to display all data',font=("Arial",15)).grid(row=8,column=0)

e_id=Entry(root)
e_id.grid(row=4,column=1)

e_fname=Entry(root)
e_fname.grid(row=4,column=3)

e_lname=Entry(root)
e_lname.grid(row=5,column=1)

e_email=Entry(root)
e_email.grid(row=5,column=3)

e_mobile=Entry(root)
e_mobile.grid(row=7,column=1)

e_tick=Entry(root)
e_tick.grid(row=8,column=1)

insert=Button(root,text="INSERT",font=("Arial",15),bg="pink",fg="black",command=insert_data).grid(row=10,column=0)

search=Button(root,text="SEARCH",font=("Arial",15),bg="pink",fg="black",command=search_data).grid(row=10,column=1)

update=Button(root,text="UPDATE",font=("Arial",15),bg="pink",fg="black",command=update_data).grid(row=10,column=2)

delete=Button(root,text="DELETE",font=("Arial",15),bg="white",fg="black",command=delete_data).grid(row=10,column=3)

display=Button(root,text="DISPLAY ALL",font=("Arial",15),bg="white",fg="black",command=display_data).grid(row=10,column=4)
