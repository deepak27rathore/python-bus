from tkinter import*
import os
from tkinter.messagebox import*
import sqlite3


e=0 #define for function edit
e1=0 
def add():
    flag=0

    if len(Operator_id.get())==0 or len(Name.get())==0 or len(Address.get())==0 or len(Email.get())==0 or len(Phone.get())==0:
        showerror('Value Missing','Enter all details')
        return

    if (Operator_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Operator id in Numeric')
        return

    if (Phone.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Phone in Numeric')
        return
    if (Name.get()).isnumeric() == 1 :
        showerror('Incorrect','Enter name in Letters')
        return
    if (Email.get()).isnumeric() == 1 :
        showerror('Incorrect','Enter Email in Letters')
        return
    


    
    #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()

     #check if operator id already exist
    cur.execute("Select Opid from operator")
    ch=cur.fetchall()
    for i in ch:
        if int(Operator_id.get())==i[0]:
            flag=1
            
    if flag==1:
        showerror('Already exist','Operator id Already exist')
        return
    else:

        #Insert Into Table
        cur.execute("INSERT INTO operator VALUES(:Opid,:Name,:Address,:Email,:Phone)",
                    {
                        'Opid':int(Operator_id.get()),
                        'Name':Name.get(),
                        'Address':Address.get(),
                        'Email':Email.get(),
                        'Phone':int(Phone.get())
                    })
        #Query to retrieve
        select_query="""Select * from operator where Opid= ?"""
        cur.execute(select_query,(Operator_id.get(),))
        out=cur.fetchall()
        print_out= '' + str(out[0][0]) +' '+ str(out[0][1])+' '+str(out[0][2]) + ' '+str(out[0][4])+' '+str(out[0][3])
        Label(root,text=print_out).grid(row=4,column=3,columnspan=6)

    
    #selection for edit 
    select_query1="""Select oid from operator where Opid= ?"""
    cur.execute(select_query1,(Operator_id.get(),))
    edit=cur.fetchall()
    global e
    e=edit[0][0]


    #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Operator_id.delete(0,END)
    Name.delete(0,END)
    Address.delete(0,END)
    Phone.delete(0,END)
    Email.delete(0,END)
    global e1
    if e1==1:
        e1=0
        showinfo('Operator Entry Update','Operator record Updated Successfully')
    else:
        showinfo('Operator Entry','Operator record added')

def edit():
    global e
    if  e==0:
        showerror('Add value','First do Add operation')
    else:
        flag=0
        #create a database or connect to one
        con=sqlite3.Connection('database.db')

        #create cursor
        cur=con.cursor()

        delete_query="""DELETE FROM operator where oid= ?"""
        cur.execute(delete_query,(e,))     
                                    

              #Commit Changes
        con.commit()

        #close Connection
        con.close()

        global e1
        e1=1

        add()
        
    
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=20)
Label(root,text='Online Bus Booking System',font='Arial 21 bold',fg='red',bg='light blue').grid(row=1,column=1,columnspan=20)
Label(root,text='Add Bus Operator Details',font='Arial 18 bold',fg='green').grid(row=2,column=1,columnspan=20,pady=20)
Label(root,text='Operator id',font='Arial 10').grid(row=3,column=0,padx=(w//6,0))
Operator_id=Entry(root)
Operator_id.grid(row=3,column=1,padx=(0,20))
Label(root,text='Name',font='Arial 10').grid(row=3,column=2)
Name=Entry(root)
Name.grid(row=3,column=3,padx=(0,20))
Label(root,text='Address',font='Arial 10').grid(row=3,column=4)
Address=Entry(root)
Address.grid(row=3,column=5,padx=(0,20))
Label(root,text='Phone',font='Arial 10').grid(row=3,column=6)
Phone=Entry(root)
Phone.grid(row=3,column=7,padx=(0,20))
Label(root,text='Email',font='Arial 10').grid(row=3,column=8)
Email=Entry(root)
Email.grid(row=3,column=9,padx=(0,20))
Button(root,text='Add',bg='green2',font='Arial 12',command=add).grid(row=3,column=10,padx=(0,20))
Button(root,text='Edit',bg='green2',font='Arial 12',command=edit).grid(row=3,column=11)
def home():
    root.destroy()
    os.startfile(".\\home.py")
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=5,column=8,pady=40)



root.mainloop()





















