from tkinter import*
import sqlite3
from tkinter.messagebox import* 
import os
root=Tk()
root.title("ONLINE BUS BOOKING")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=20,padx=w//2.5)
Label(root,text='ONLINE BUS BOOKING SYSTEM',font='Arial 18 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=20)
Label(root,text='CHECK YOUR BOOKING',font='Arial 18 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20,columnspan=20)
Label(root,text='Enter your Mobile No.',font="14").grid(row=3,column=1,padx=(w//3.3,0))
Mobile_No=Entry(root)
Mobile_No.grid(row=3,column=2)
def fun():
    if (Mobile_No.get()).isnumeric() == 0:
            showerror('Incorrect','Enter Mobile number in Numeric')
            return
    if len(Mobile_No.get())!=10:
        showerror('Invalid','Invalid phone number Enter 10 digit number')
        return
    #create a database or connect to one
    con=sqlite3.Connection('database.db')
    #create cursor
    cur=con.cursor()

    cur.execute("SELECT * FROM booking where Mobile= ?",(int(Mobile_No.get()),))
    res=cur.fetchall()
    if len(res)==0:
        showinfo('Unavilable','Ticket Not exist')
        return
    ticket=Frame(root,relief='groove',bd=5)
    ticket.grid(row=4,column=0,columnspan=20,pady=(20,0))
    Label(ticket,text='Passengers:',font='7').grid(row=0,column=0)
    Label(ticket,text=res[0][0],font='7').grid(row=0,column=1)
    Label(ticket,text='Gender:',font='7').grid(row=0,column=2)
    Label(ticket,text=res[0][1],font='7').grid(row=0,column=3)
    Label(ticket,text='No. of seats:',font='7').grid(row=1,column=0)
    Label(ticket,text=str(res[0][2]),font='7').grid(row=1,column=1)
    Label(ticket,text='Phone:',font='7').grid(row=1,column=2)
    Label(ticket,text=str(res[0][3]),font='7').grid(row=1,column=3)
    Label(ticket,text='Age:',font='7').grid(row=2,column=0)
    Label(ticket,text=str(res[0][4]),font='7').grid(row=2,column=1)
    Label(ticket,text='Fare Rs:',font='7').grid(row=2,column=2)
    cur.execute('SELECT Fare from bus where Busid= ?',(res[0][5],))
    ish=cur.fetchall()
    fare1=ish[0][0]*res[0][2]
    Label(ticket,text=str(fare1),font='7').grid(row=2,column=3)
    Label(ticket,text='Booking Ref.',font='7').grid(row=3,column=0)
    cur.execute("SELECT oid FROM booking where Mobile= ?",(int(Mobile_No.get()),))
    r=cur.fetchall()
    Label(ticket,text=str(r[0][0]),font='7').grid(row=3,column=1)
    Label(ticket,text='Travel On:',font='7').grid(row=4,column=0)
    Label(ticket,text=res[0][6],font='7').grid(row=4,column=1)
    Label(ticket,text='Boarding Point:',font='7').grid(row=5,column=2)
    Label(ticket,text=res[0][7],font='7').grid(row=5,column=3)
    Label(ticket,text='Destination Point:',font='7').grid(row=6,column=0)
    Label(ticket,text=res[0][8],font='7').grid(row=6,column=1)
    Label(ticket,text='Total amount Rs.' + str(fare1) + '.00 /- to be paid at the time of boarding the bus').grid(row=7,column=0,columnspan=10)
Button(root,text='Check your booking',command=fun).grid(row=3,column=3,padx=20)
root.mainloop()
