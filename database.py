#from tkinter import*
import sqlite3
#root=Tk()
#root.title("DATABASE OF BUS BOOKING")
#root.geometry("400x500")

#Databases

#create a database or connect to one
con=sqlite3.Connection('database.db')

#create cursor
cur=con.cursor()


#create table

#Operator table
cur.execute(""" CREATE TABLE operator(
            Opid number,
            Name text,
            Address text,
            Email text,
            Phone number)""")

#Bus table
cur.execute(""" CREATE TABLE bus(
            Busid number,
            Type text,
            Capacity number,
            Fare number,
            Rid number,
            Opid number)""")
#Run table
cur.execute(""" CREATE TABLE run(
                Busid number,
                Date text,
                seat_a number)""")
#Route table
cur.execute(""" CREATE TABLE route(
             Rid number,
             stationid number,
             station_name text)""")

#Booking history table
cur.execute(""" CREATE TABLE booking(
            Name text,
            Gender text,
            No_of_seats number,
            Mobile number,
            Age number,
            Busid number,
            Date text,
            Frpoint text,
            Topoint text)""")

#Commit Changes
con.commit()

#close Connection
con.close()

#root.mainloop() 
