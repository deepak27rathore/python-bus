from tkinter import*
import os
root=Tk()
root.title('ONLINE BUS BOOKING')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=6)
Label(root,text='ONLINE BUS BOOKING SYSTEM',font='Arial 25 bold',bg='light blue',fg='red').grid(row=1,column=6,pady=(0,40))
def seatbooking():
    root.destroy()
    os.startfile(".\\seatbooking.py")
Button(root,text='Seat Booking',font='Arial 14',fg='black',bg='light green',command=seatbooking).grid(row=6,column=2,padx=(w//3.5,0))
def check():
    root.destroy()
    os.startfile(".\\checkseat.py")
Button(root,text='Check Booked Seat',font='Arial 14',fg='black',bg='green2',command=check).grid(row=6,column=6)
def nextpage():
    root.destroy()
    os.startfile("addbusdetails.py")
Button(root,text='Add Bus Details',font='Arial 14',fg='black',bg='green3',command=nextpage).grid(row=6,column=7)
Label(root,text="").grid(row=7,column=0)
Label(root,text="For Admin Only",font='15',fg='red').grid(row=8,column=7)

root.mainloop()
