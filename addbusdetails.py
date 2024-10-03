from tkinter import*
import os
root=Tk()
root.title("ONLINE BUS BOOKING")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=20,padx=w//2.5)
Label(root,text='ONLINE BUS BOOKING SYSTEM',font='Arial 22 bold',bg='light blue',fg='red').grid(row=1,column=0,columnspan=20,pady=(0,20))
Label(root,text='Add New Details To Bus',font='Arial 20 bold',fg='green').grid(row=2,column=0,pady=(0,20),columnspan=20)
def newoperator():
    root.destroy()
    os.startfile(".\\newoperator.py")
def newbus():
    root.destroy()
    os.startfile(".\\newbus.py")
def newroute():
    root.destroy()
    os.startfile(".\\newroute.py")
def newrun():
    root.destroy()
    os.startfile(".\\newrun.py")
Button(root,text='New Operator',bg='light green',font='18',command=newoperator).grid(row=3,column=0,padx=(w//3.3,0))
Button(root,text='New Bus',bg='tomato',font='18',command=newbus).grid(row=3,column=1,padx=30)
Button(root,text='New Route',bg='light blue',font='18',command=newroute).grid(row=3,column=2,padx=(0,30))
Button(root,text='New Run',bg='pale violet red',font='18',command=newrun).grid(row=3,column=3)

root.mainloop()
