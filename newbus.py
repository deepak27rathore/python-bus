from tkinter import*
import os
from tkinter.messagebox import*
import sqlite3
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

'''#Bus table
cur.execute(""" CREATE TABLE bus(
            Busid number,
            Type text,
            Capacity number,
            Fare number,
            Rid number,
            Opid number)""")'''
e=0
e1=0
def add():
    flag=0
    flag2=0
    flag3=0


    if len(Bus_id.get())==0 or len(Capacity.get())==0 or len(Fare_Rs.get())==0 or len(Route_id.get())==0 or len(Operator_id.get())==0:
        showerror('Value Missing','Enter all details')
        return
    if Bus_type.get()=='Select Bus type':
        showerror('Value Missing','Select Bus type')
        return

    if (Bus_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Bus id in Numeric')
        return

    if (Capacity.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Capacity in Numeric')
        return
    if (Fare_Rs.get()).isnumeric() == 0 :
        showerror('Incorrect','Enter Fare in Letters')
        return
    if (Route_id.get()).isnumeric() == 0 :
        showerror('Incorrect','Enter Route id in Letters')
        return
    if (Operator_id.get()).isnumeric() == 0 :
        showerror('Incorrect','Enter Operator id in Letters')
        return
    
    #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()

    
     #check if operator id not exist
    cur.execute("Select Opid from operator")
    ch1=cur.fetchall()
    for i in ch1:
        if int(Operator_id.get())==i[0]:
            flag2=1
            
    if flag2==0:
        showerror('Not exist',"""Operator doesn't exist First add operator
        Or use different Operator""")
        return

    #check if route id not exist
    cur.execute("Select Rid from route")
    ch2=cur.fetchall()
    for i in ch2:
        if int(Route_id.get())==i[0]:
            flag3=1
            
    if flag3==0:
        showerror('Not exist',"""Route doesn't exist First add Route
        Or use different Route""")
        return

     #check if Bus id already exist
    cur.execute("Select Busid from bus")
    ch=cur.fetchall()
    for i in ch:
        if int(Bus_id.get())==i[0]:
            flag=1
            
    if flag==1:
        showerror('Already exist','Bus id Already exist')
        return
    else:

        #Insert Into Table
        cur.execute("INSERT INTO bus VALUES(:Busid,:Type,:Capacity,:Fare,:Rid,:Opid)",
                    {
                        'Busid':int(Bus_id.get()),
                        'Type':Bus_type.get(),
                        'Capacity':int(Capacity.get()),
                        'Fare':int(Fare_Rs.get()),
                        'Rid':int(Route_id.get()),
                        'Opid':int(Operator_id.get())
                    })
        #Query to retrieve
        select_query="""Select * from bus where Busid= ?"""
        cur.execute(select_query,(Bus_id.get(),))
        out=cur.fetchall()
        print_out= 'Bus id : ' + str(out[0][0]) +'   Bus type :  '+ str(out[0][1])+'   Capacity :  '+str(out[0][2]) + '   Fare : '+str(out[0][3])+'   Operator id : '+str(out[0][5])+'  Route id :  '+str(out[0][4])
        Label(root,text=print_out).grid(row=4,column=1,columnspan=10)        

    #selection for edit 
    select_query1="""Select oid from bus where Busid= ?"""
    cur.execute(select_query1,(Bus_id.get(),))
    edit=cur.fetchall()
    global e
    e=edit[0][0]


    #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Bus_id.delete(0,END)
    Bus_type.set('Select Bus type')
    Capacity.delete(0,END)
    Fare_Rs.delete(0,END)
    Route_id.delete(0,END)
    Operator_id.delete(0,END)
    global e1
    if e1==1:
        e1=0
        showinfo('Bus Entry Update','Bus record Updated Successfully')
    else:
        showinfo('Bus Entry','Bus record added')

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

        delete_query="""DELETE FROM bus where oid= ?"""
        cur.execute(delete_query,(e,))     
                                    

        #Commit Changes
        con.commit()

        #close Connection
        con.close()

        global e1
        e1=1

        add()




img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=20)
Label(root,text='Online Bus Booking System',font='Arial 21 bold',fg='red',bg='light blue').grid(row=1,column=1,columnspan=20)
Label(root,text='Add Bus Details',font='Arial 18 bold',fg='green').grid(row=2,column=1,columnspan=20,pady=20)
Label(root,text='Bus ID',font='Arial 10').grid(row=3,column=0,padx=(w//6,0))
Bus_id=Entry(root)
Bus_id.grid(row=3,column=1,padx=(0,20))

Label(root,text='Bus Type',font='Arial 10').grid(row=3,column=2)
Bus_type=StringVar()
opt=['AC 2X2','AC 3X2','Non AC 3X2','AC Sleeper 2X1','Non AC Sleeper 2X1']
Bus_type.set('Select Bus type')
d_menu=OptionMenu(root,Bus_type,*opt,).grid(row=3,column=3,padx=(0,15))

Label(root,text='Capacity',font='Arial 10').grid(row=3,column=4)
Capacity=Entry(root)
Capacity.grid(row=3,column=5,padx=(0,20))
Label(root,text='Fare Rs',font='Arial 10').grid(row=3,column=6)
Fare_Rs=Entry(root)
Fare_Rs.grid(row=3,column=7,padx=(0,20))
Label(root,text='Operator ID',font='Arial 10').grid(row=3,column=8)
Operator_id=Entry(root)
Operator_id.grid(row=3,column=9,padx=(0,20))
Label(root,text='Route id',font='Arial 10').grid(row=3,column=9)
Route_id=Entry(root)
Route_id.grid(row=3,column=10,padx=(0,20))
Button(root,text='Add',bg='green3',font='Arial 12',command=add).grid(row=5,column=6,padx=(0,20))
Button(root,text='Edit',bg='green3',font='Arial 12',command=edit).grid(row=5,column=7,padx=30)
def home():
    root.destroy()
    os.startfile(".\\home.py")
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=5,column=8,pady=40)
root.mainloop()

