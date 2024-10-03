from tkinter import*
import os
from datetime import datetime
from tkinter.messagebox import*
import sqlite3
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

'''cur.execute(""" CREATE TABLE run(
                Busid number,
                Date text
                seat_a number)""")'''
def valDate(input1):

    try:
        dateObject = datetime.strptime(input1,'%d/%m/%Y')
        return 1
    except ValueError:
        return 0
    
def add():
     #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()
    
    flag3=0
    flag=0
    if len(Bus_id.get())==0 or len(Running_Date.get())==0 or len(Seat_Available.get())==0 :
        showerror('Value Missing','Enter all details')
        return

    if (Bus_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Bus id in Numeric')
        return

    if (Seat_Available.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Seat_Available in Numeric')
        return

    cur.execute('Select Capacity from bus where Busid=?',(Bus_id.get(),))
    er=cur.fetchall()
    if int(Seat_Available.get())>er[0][0]:
        showerror('Unappropriate','Input Available less than Capacity')
        return

    input1=valDate(Running_Date.get())
    if input1==0:
        showerror('Incorrect',"""Enter Date in Correct way
        DD/MM/YY
    Or Enter correct Date""")
        return

    

    #check if Bus id not exist
    cur.execute("Select Busid from bus")
    ch2=cur.fetchall()
    for i in ch2:
        if int(Bus_id.get())==i[0]:
            flag3=1
            
    if flag3==0:
        showerror('Not exist',"""Bus doesn't exist First add Bus
        Or use different Bus""")
        return

    #check if already record exist
    cur.execute("Select Busid ,Date from run")
    ch=cur.fetchall()
    for i in ch:
        if int(Bus_id.get())==i[0] and int(Date.get())==i[1]:
            flag=1
            
    if flag==1:
        showerror('Already exist','Record Already exist')
        return

    


     #Insert Into Table
    cur.execute("INSERT INTO run VALUES(:Bid,:Date,:seat)",
                    {
                        'Bid':int(Bus_id.get()),
                        'Date':Running_Date.get(),
                        'seat':int(Seat_Available.get())
                    })
      #Query to retrieve
    select_query="""Select * from run where Busid= ? AND Date=?"""
    cur.execute(select_query,(Bus_id.get(),Running_Date.get()))
    out=cur.fetchall()
    print_out= 'Bus id: ' + str(out[0][0]) +' Date :  '+ str(out[0][1])+' Seat available : '+str(out[0][2]) 
    Label(root,text=print_out).grid(row=4,column=2,columnspan=6)
        
    #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Bus_id.delete(0,END)
    Running_Date.delete(0,END)
    Seat_Available.delete(0,END)

def deleter():
    flag=0
    if len(Bus_id.get())==0 or len(Running_Date.get())==0 or len(Seat_Available.get())==0 :
        showerror('Value Missing','Enter all details')
        return

    if (Bus_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Bus id in Numeric')
        return

    if (Seat_Available.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Seat_Available in Numeric')
        return

    input1=valDate(Running_Date.get())
    if input1==0:
        showerror('Incorrect',"""Enter Date in Correct way
        DD/MM/YY
    Or Enter correct Date""")
        return

     #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()
    cur.execute("Select Busid ,Date from run")
    ch=cur.fetchall()
    for i in ch:
        if int(Bus_id.get())==i[0] and (Running_Date.get())==i[1]:
            flag=1

    if flag==0:
        showerror('Not Exist','No such record exist')
    else:
        cur.execute("DELETE FROM run where Busid= ? and Date= ?""",(Bus_id.get(),(Running_Date.get())))
        showinfo('Record Deleted','Record deleted successfully')
        
      #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Bus_id.delete(0,END)
    Running_Date.delete(0,END)
    Seat_Available.delete(0,END)


    

img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=20)
Label(root,text='Online Bus Booking System',font='Arial 21 bold',fg='red',bg='light blue').grid(row=1,column=1,columnspan=20)
Label(root,text='Add Bus Running Details',font='Arial 18 bold',fg='green').grid(row=2,column=1,columnspan=20,pady=(20,40))
Label(root,text='Bus ID',font='Arial 12').grid(row=3,column=0,padx=(w//6,0))
Bus_id=Entry(root)
Bus_id.grid(row=3,column=1,padx=(0,20))

Label(root,text='Running Date',font='Arial 12').grid(row=3,column=2)
Running_Date=Entry(root)
Running_Date.grid(row=3,column=3,padx=(0,20))

Label(root,text='Seat Available',font='Arial 12').grid(row=3,column=4)
Seat_Available=Entry(root)
Seat_Available.grid(row=3,column=5,padx=(0,20))

Button(root,text='Add Run',bg='green2',font='Arial 12',command=add).grid(row=3,column=6,padx=(0,20))
Button(root,text='Delete Run',bg='green2',font='Arial 12',command=deleter).grid(row=3,column=7,padx=30)
def home():
    root.destroy()
    os.startfile(".\\home.py")
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=5,column=5,pady=40)
root.mainloop()
