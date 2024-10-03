from tkinter import*
import os
from tkinter.messagebox import*
import sqlite3
root=Tk()
root.title("ONLINE BUS BOOKING")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')

#create a database or connect to one
con=sqlite3.Connection('database.db')

#create cursor
cur=con.cursor()
cur.execute('SELECT * from booking')
see=cur.fetchall()
bo=0
for i in see:
    a=i
    bo+=1
Label(root,image=img).grid(row=0,column=0,columnspan=20,padx=w//2.5)
Label(root,text='ONLINE BUS BOOKING SYSTEM',font='Arial 18 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=20)
Label(root,text='Bus ticket',font='10').grid(row=2,column=0,columnspan=20,pady=(20,0))
ticket=Frame(root,relief='groove',bd=5)
ticket.grid(row=3,column=0,columnspan=20,pady=(20,0))
Label(ticket,text='Passenger:',font='7').grid(row=0,column=0)
Label(ticket,text=a[0],font='7').grid(row=0,column=1)
Label(ticket,text='Gender:',font='7').grid(row=0,column=2)
Label(ticket,text=a[1],font='7').grid(row=0,column=3)
Label(ticket,text='No. of seats:',font='7').grid(row=1,column=0)
Label(ticket,text=str(a[2]),font='7').grid(row=1,column=1)
Label(ticket,text='Phone:',font='7').grid(row=1,column=2)
Label(ticket,text=str(a[3]),font='7').grid(row=1,column=3)
Label(ticket,text='Age:',font='7').grid(row=2,column=0)
Label(ticket,text=str(a[4]),font='7').grid(row=2,column=1)
Label(ticket,text='Fare Rs:',font='7').grid(row=2,column=2)
cur.execute('SELECT Fare from bus where Busid= ?',(a[5],))
ish=cur.fetchall()
fare1=ish[0][0]*a[2]
Label(ticket,text=str(fare1),font='7').grid(row=2,column=3)
Label(ticket,text='Booking Ref.',font='7').grid(row=3,column=0)
Label(ticket,text=str(bo),font='7').grid(row=3,column=1)
Label(ticket,text='Bus Detail:',font='7').grid(row=3,column=2)
cur.execute("""SELECT Opid FROM bus where Busid = ? """,(a[5],))
out5=cur.fetchall()
cur.execute("""SELECT Name FROM  operator where Opid=?""",(out5[0][0],))
out6=cur.fetchall()
Label(ticket,text=out6[0][0],font='7').grid(row=3,column=3)
Label(ticket,text='Travel On:',font='7').grid(row=4,column=0)
Label(ticket,text=a[6],font='7').grid(row=4,column=1)
Label(ticket,text='Booked On:',font='7').grid(row=4,column=2)
Label(ticket,text='Nov 30, 2020',font='7').grid(row=4,column=3)
Label(ticket,text='No. of seats:',font='7').grid(row=5,column=0)
Label(ticket,text=str(a[2]),font='10').grid(row=5,column=1)
Label(ticket,text='Boarding Point:',font='7').grid(row=5,column=2)
Label(ticket,text=a[7],font='7').grid(row=5,column=3)
Label(ticket,text='Total amount Rs.' + str(fare1) + '.00 /- to be paid at the time of boarding the bus').grid(row=6,column=0,columnspan=10)
showinfo('Success','Seat Booked')
 #Commit Changes
con.commit()

#close Connection
con.close()
root.mainloop()

