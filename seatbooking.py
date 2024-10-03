from tkinter import*
import os
from tkinter.messagebox import*
from datetime import datetime
import sqlite3
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=20)
Label(root,text='ONLINE BUS BOOKING SYSTEM',font='Arial 18 bold',bg='light blue',fg='red').grid(row=1,column=1,columnspan=20)
Label(root,text='Enter Journey Details',font='Arial 14',fg='dark green',bg='light green').grid(row=2,column=1,pady=20,columnspan=20)
Label(root,text="To",font='Arial').grid(row=3,column=0,padx=(w//3.5,0))
To=Entry(root)
To.grid(row=3,column=1,padx=(0,15))
Label(root,text="From",font='Arial').grid(row=3,column=2)
From=Entry(root)
From.grid(row=3,column=3,padx=(0,15))
Label(root,text='Journey date',font='Arial').grid(row=3,column=4)
Journey_date=Entry(root)
Journey_date.grid(row=3,column=5,padx=(0,15))

def valDate(input1):

    try:
        dateObject = datetime.strptime(input1,'%d/%m/%Y')
        return 1
    except ValueError:
        return 0

Bus_No=IntVar()
def fun():
    flag=0
    flag1=0
    if len(To.get())==0 or len(From.get())==0 or len(Journey_date.get())==0:
        showerror('Value Missing','Please Enter all Details')
        return
        
    if (To.get()).isnumeric() == 1 :
        showerror('Incorrect','To name in Letters')
        return
    if (From.get()).isnumeric() == 1 :
        showerror('Incorrect','From Email in Letters')
        return
    
    input1=valDate(Journey_date.get())
    if input1==0:
        showerror('Incorrect',"""Enter Date in Correct way
        DD/MM/YY
    Or Enter correct Date""")
        return
    

    #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()

    cur.execute("""SELECT rid,stationid FROM route where station_name= ?""",(To.get(),))
    out1=cur.fetchall()
    if len(out1)==0:
        showinfo('Not exist','No Bus available')
        return
    cur.execute("""SELECT rid,stationid FROM route where station_name= ?""",(From.get(),))
    out2=cur.fetchall()
    if len(out2)==0:
        showinfo('Not exist','No Bus available')
        return
    for i in out1:
        for j in out2:
            if i[0]==j[0] and j[1]<i[1]:
                flag=i[0]
                break
        if flag!=0:
            break
    if flag==0:
        showinfo('Not exist','NO Bus available')
        return
    cur.execute("""SELECT Busid FROM bus where Rid=?""",(flag,))
    out3=cur.fetchall()
    if len(out3)==0:
        showinfo('Not exist','No Bus available')
        return
    cur.execute("""SELECT Date FROM run where Busid=? """,(out3[0][0],))
    ree=cur.fetchall()
    for i in ree:
        if Journey_date.get()==i[0]:
            flag1=1
    if flag1==0:
        showerror('Unavilable','No Bus available on this date')
        return
        
    cur.execute("""SELECT Date,Busid FROM run where Busid=? """,(out3[0][0],))
    out4=cur.fetchall()
    if len(out4)==0:
        showinfo('Not exist','No Bus available')
        return
        
    

    show_bus=Frame(root )
    show_bus.grid(row=4,column=0,padx=(100,0),columnspan=8)
    Label(show_bus,text='Select Bus',fg='green',font='14').grid(row=0,column=0,padx=25)
    Label(show_bus,text='Operator',fg='green',font='14').grid(row=0,column=1,padx=25)
    Label(show_bus,text='Bus Type',fg='green',font='14').grid(row=0,column=2,padx=25)
    Label(show_bus,text='Available/Capacity',fg='green',font='14').grid(row=0,column=3,padx=25)
    Label(show_bus,text='Fare',fg='green',font='14').grid(row=0,column=4,padx=25)
    count=1
    for i in out4:
        Radiobutton(show_bus,text='Bus ' + str(i[1]),variable=Bus_No,value=i[1],indicator=0,bg='wheat1').grid(row=count,column=0,padx=25)
        cur.execute("""SELECT Opid FROM bus where Busid = ? """,(i[1],))
        out5=cur.fetchall()
        cur.execute("""SELECT Name FROM  operator where Opid=?""",(out5[0][0],))
        out6=cur.fetchall()
        Label(show_bus,text=out6[0][0],font='10',fg='blue').grid(row=count,column=1,padx=25)
        cur.execute("""SELECT Type FROM bus where Busid=? """,(i[1],))
        out7=cur.fetchall()
        Label(show_bus,text=out7[0][0],font='10',fg='blue').grid(row=count,column=2,padx=25)
        cur.execute("""SELECT Capacity FROM bus where Busid=? """,(i[1],))
        out8=cur.fetchall()
        cur.execute("""SELECT seat_a FROM run where Busid=? """,(i[1],))
        out9=cur.fetchall()
        Label(show_bus,text=str(out9[0][0]) + '/' +str(out8[0][0]) ,font='10',fg='blue').grid(row=count,column=3,padx=25)
        cur.execute("""SELECT Fare FROM bus where Busid=? """,(i[1],))
        out10=cur.fetchall()
        Label(show_bus,text=out10[0][0],font='10',fg='blue').grid(row=count,column=4,padx=25)
        count+=1
        
        
        
    Button(show_bus,text="Proceed to Book",font="Arial",bg='light green',command=fun1).grid(row=1,column=7,padx=25)

     #Commit Changes
    con.commit()

    #close Connection
    con.close()
    
Button(root,text="Show Bus",font="Arial",bg='light green',command=fun).grid(row=3,column=6,padx=(0,15))
def home():
    root.destroy()
    os.startfile(".\\home.py")
home_img=PhotoImage(file='.\\home.png')
Button(root,image=home_img,command=home).grid(row=3,column=7)



def fun1():
    if Bus_No.get()==0:
        showerror('Value Missing','Please Select Bus')
        return
    #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()
    cur.execute("""SELECT seat_a FROM run where Busid=? """,(Bus_No.get(),))
    www=cur.fetchall()
    if www[0][0]==0:
        showerror("Can't Book","Seats Not Available")
        return
    
    passenger_details=Frame(root)
    passenger_details.grid(row=5,column=0,padx=(100,0),columnspan=8,pady=(30,0))
    Label(passenger_details,text='Fill Passenger Details  to book the bus ticket',font='Arial 18 bold',bg='light blue',fg='red').grid(row=0,column=0,columnspan=20,pady=(0,20))
    Label(passenger_details,text='Name',font='14').grid(row=1,column=0)
    Name=Entry(passenger_details)
    Name.grid(row=1,column=1,padx=(0,15))
    Label(passenger_details,text='Gender',font='14').grid(row=1,column=3)
    gender=StringVar()
    opt=['Male','Female','Transgender']
    gender.set('Gender')
    d_menu=OptionMenu(passenger_details,gender,*opt,).grid(row=1,column=4,padx=(0,15))
    Label(passenger_details,text='No. of seats',font='14').grid(row=1,column=5)
    No_of_seats=Entry(passenger_details)
    No_of_seats.grid(row=1,column=6,padx=(0,15))
    Label(passenger_details,text='Mobile no.',font='14').grid(row=1,column=7)
    Mobile_No=Entry(passenger_details)
    Mobile_No.grid(row=1,column=8,padx=(0,15))
    Label(passenger_details,text='Age',font='14').grid(row=1,column=9)
    Age=Entry(passenger_details)
    Age.grid(row=1,column=10,padx=(0,15))
    def fun3():
         
        if len(Name.get())==0 or len(No_of_seats.get())==0 or len(Mobile_No.get())==0 or len(Age.get())==0:
            showerror('Value Missing','Please Enter all Details')
            return
        if gender.get()=='Gender':
            showerror('Selection pending','Please Select Gender')
            return

        if (Name.get()).isnumeric() == 1 :
            showerror('Incorrect','Enter name in Letters')
            return

        if (No_of_seats.get()).isnumeric() == 0:
            showerror('Incorrect','Enter No. of seats in Numeric')
            return

        if (Mobile_No.get()).isnumeric() == 0:
            showerror('Incorrect','Enter Mobile number in Numeric')
            return
        if len(Mobile_No.get())!=10:
            showerror('Invalid','Invalid phone number Enter 10 digit number')
            return

        if (Age.get()).isnumeric() == 0 :
            showerror('Incorrect','Enter Age  in Numeric')
            return
        if int(Age.get())<18 or int(Age.get())>80:
            showerror('Invalid','Enter age between 18 to 80')
            return 
        if int(No_of_seats.get())>www[0][0]:
            showerror('Invalid seats','Enter seats in range of availability')
            return

        #create a database or connect to one
        con=sqlite3.Connection('database.db')

        #create cursor
        cur=con.cursor()
        

        cur.execute("""SELECT Fare FROM bus where Busid=? """,(Bus_No.get(),))
        chfar=cur.fetchall()
        var1=(int(No_of_seats.get()))*(chfar[0][0])

        ddd=askyesno("Fare confirm ","Total Amount to be paid Rs. " + str(var1) + ".00" )
        if ddd==0:
            return
                                      
                                      
                                      
                     

        #Insert Into Table
        cur.execute("INSERT INTO booking VALUES(:Name,:Gender,:nos,:Mobile,:Age,:Busid,:Date,:Frpoint,:Topoint)",
                    {
                        'Name':Name.get(),
                        'Gender':gender.get(),
                        'nos':int(No_of_seats.get()),
                        'Mobile':int(Mobile_No.get()),
                        'Age':int(Age.get()),
                        'Busid':Bus_No.get(),
                        'Date':Journey_date.get(),
                        'Frpoint':From.get(),
                        'Topoint':To.get()
                                  
                    })

        cur.execute("UPDATE run SET seat_a = ? where Busid=? """,(www[0][0]-int(No_of_seats.get()),Bus_No.get()))

        
         #Commit Changes
        con.commit()

        #close Connection
        con.close()

        # clear the text boxes
        Name.delete(0,END)
        gender.set('Gender')
        No_of_seats.delete(0,END)
        Mobile_No.delete(0,END)
        Age.delete(0,END)

        
        root.destroy()
        os.startfile(".\\seatbooked.py")

    Button(passenger_details,text='Book Seat',command=fun3,font="Arial",bg='light green').grid(row=1,column=11)
root.mainloop()




