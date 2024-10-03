from tkinter import*
import os
from tkinter.messagebox import*
import sqlite3
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

'''cur.execute(""" CREATE TABLE route(
             Rid number,
             stationid number,
             station_name text)""")'''

def Addroute():
    flag=0
    if len(Route_id.get())==0 or len(Station_name.get())==0 or len(Station_id.get())==0:
        showerror('Value Missing','Enter all details')
        return

    if (Route_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Route id in Numeric')
        return

    if (Station_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Station id in Numeric')
        return
    if (Station_name.get()).isnumeric() == 1 :
        showerror('Incorrect','Enter Station name in Letters')
        return

    #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()

    
     #check if operator id already exist
    cur.execute("Select Rid ,stationid from route")
    ch=cur.fetchall()
    for i in ch:
        if int(Route_id.get())==i[0] and int(Station_id.get())==i[1]:
            flag=1
            
    if flag==1:
        showerror('Already exist','Record Already exist')
        return
    else:

        #check if operator id already exist
        

        #Insert Into Table
        cur.execute("INSERT INTO route VALUES(:rid,:sid,:sname)",
                    {
                        'rid':int(Route_id.get()),
                        'sname':Station_name.get(),
                        'sid':int(Station_id.get())
                    })
         #Query to retrieve
        select_query="""Select * from route where Rid= ? and stationid= ?"""
        cur.execute(select_query,(Route_id.get(),(Station_id.get())))
        out=cur.fetchall()
        print_out= 'Route id : ' + str(out[0][0]) +'  Station name : '+ str(out[0][2])+' Station id : '+str(out[0][1]) 
        Label(root,text=print_out).grid(row=4,column=1,columnspan=6)


    #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Route_id.delete(0,END)
    Station_name.delete(0,END)
    Station_id.delete(0,END)
    showinfo('Route Entry','Route record added')
    
def deleter():
    flag=0
    if len(Route_id.get())==0 or len(Station_name.get())==0 or len(Station_id.get())==0:
        showerror('Value Missing','Enter all details')
        return

    if (Route_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Route id in Numeric')
        return

    if (Station_id.get()).isnumeric() == 0:
        showerror('Incorrect','Enter Station id in Numeric')
        return
    if (Station_name.get()).isnumeric() == 1 :
        showerror('Incorrect','Enter Station name in Letters')
        return

     #create a database or connect to one
    con=sqlite3.Connection('database.db')

    #create cursor
    cur=con.cursor()
    cur.execute("Select Rid ,stationid from route")
    ch=cur.fetchall()
    for i in ch:
        if int(Route_id.get())==i[0] and int(Station_id.get())==i[1]:
            flag=1

    if flag==0:
        showerror('Not Exist','No such record exist')
    else:
        cur.execute("DELETE FROM route where Rid= ? and stationid= ?""",(Route_id.get(),(Station_id.get())))
        showinfo('Record Deleted','Record deleted successfully')
        
      #Commit Changes
    con.commit()

    #close Connection
    con.close()

    # clear the text boxes
    Route_id.delete(0,END)
    Station_name.delete(0,END)
    Station_id.delete(0,END)






img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=1,columnspan=20)
Label(root,text='Online Bus Booking System',font='Arial 21 bold',fg='red',bg='light blue').grid(row=1,column=1,columnspan=20)
Label(root,text='Add Bus Route Details',font='Arial 18 bold',fg='green').grid(row=2,column=1,columnspan=20,pady=20)
Label(root,text='Route id',font='Arial 10').grid(row=3,column=0,padx=(w//5,0))
Route_id=Entry(root)
Route_id.grid(row=3,column=1,padx=(0,20))
Label(root,text='Station Name',font='Arial 10').grid(row=3,column=2)
Station_name=Entry(root)
Station_name.grid(row=3,column=3,padx=(0,20))
Label(root,text='Station id',font='Arial 10').grid(row=3,column=4)
Station_id=Entry(root)
Station_id.grid(row=3,column=5,padx=(0,20))
Button(root,text='Add Route',bg='green2',font='Arial 12',command=Addroute).grid(row=3,column=6,padx=(0,20))
Button(root,text='Delete Route',bg='green2',font='Arial 12',fg='red',command=deleter).grid(row=3,column=7,padx=30)
def home():
    root.destroy()
    os.startfile(".\\home.py")
img1=PhotoImage(file='.\\home.png')
Button(root,image=img1,command=home).grid(row=5,column=4,pady=40)
root.mainloop()
