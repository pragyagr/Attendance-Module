from Tkinter import *
import tkMessageBox
import serial
import MySQLdb
import time

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="student") # name of the data base

#read id from fingerprint sensor
device = 'COM4'
flag = 0

def onclick_view():
    def getvalue():
        E1_data = v1.get()
        E2_data = v2.get()
        print '%s' %E1_data
    win1.destroy()
    
    win2=Tk()
    win2.title("Attendance Module")
    win2.geometry('250x250')

    v1 = StringVar()
    v2 = StringVar()
    v1.set("mm/dd/yy")
    v2.set("mm/dd/yy")

    list=[]

    showcol_query = "select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA= 'student' and TABLE_NAME = 'attendance'"
    cur = db.cursor()
    cur.execute(showcol_query)
    a = cur.fetchall()
    a
    #for i in range(2,len(a)-1):
        #list.append(a[i][0])
     #   print list
    L = Label(win2, text="Subject: %s" %variable.get() ).pack()    
    L2= Label(win2, text="From:").pack()
    #E1 = Entry(win2, textvariable = v1).pack()
    from_option = OptionMenu(win2, v1, "date").pack()
    L3= Label(win2, text="To:").pack()
    to_option = OptionMenu(win2, v2,"date" ).pack()
    #E2 = Entry(win2, textvariable = v2).pack()
    
    button3 = Button(win2, text="OK", command = getvalue ).pack()

    win2.mainloop()

def onclick_mark():
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    
    date = time.strftime("%x")
    cur.execute("SHOW COLUMNS FROM attendance LIKE '%s'" %date) # code for adding column when it doesn't exist 
    exist = cur.fetchone()                                      # code for adding column when it doesn't exist 
    if exist is None:                                           # code for adding column when it doesn't exist 
        cur.execute("ALTER TABLE attendance ADD `%s` INT(2) NOT NULL DEFAULT '0'" %date)    
    
    def onclick_next():
        try:
            v3_value = int(v3.get())
        except:
            error_msg = 'number you entered is not an integer'
            label_err = Label (win3, text=error_msg, fg='red').pack()
        '''flag=0
        while 1:
            if flag==0:
                try:
                    err1 = "Trying...", device
                    lab1 = Label(win3, text=err1).pack()
                    arduino = serial.Serial(device, 9600)
                    flag = 1
                except:
                    err2 = "Failed to connect on ", device
                    lab2 = Label(win3, text=err2).pack()
                    flag = 0
            if flag==1:
                try:
                    my_id = arduino.readline()   #read the data from arduino
                    if my_id != -2:
                        try:
                            cur.execute("UPDATE attendance SET `%s`= %d WHERE Roll_Number=(SELECT Roll_Number FROM student_att WHERE Id= %d)" %(date,v3_value, int(my_id)))
                        except:
                            err3 = 'Failed to read from arduino. Try burning the code to arduino again'
                            lab3 = Label(win3, text=err3).pack()
                except:
                    print "Failed to get data from Arduino!"
                    flag = 0;'''
        db.commit()
    #if my_id != -2:
        #try:
        #cur.execute("UPDATE attendance SET `%s`='1' WHERE Roll_Number=(SELECT Roll_Number FROM student_att WHERE Id= %d)" %(date, my_id))
       # except:
           # print 'Failed to read from arduino. Try burning the code to arduino again'
    #db.commit()

    
    win1.destroy()
    win3 = Tk()
    win3.title("Attendance Module")

    L = Label(win3, text="Subject: %s" %variable.get() ).pack()
    
    lab1 = Label(win3, text="How many classes are there today?").pack()
    v3 = StringVar()
    v3.set("1")
    ent1 = Entry(win3, textvariable=v3).pack()

    L3= Label(win3, text="progress bar").pack()
    button_ok = Button(win3, text="Next", command= onclick_next).pack()
    win3.geometry('250x250')
    win3.mainloop()

win1 = Tk()
win1.geometry('500x500')
win1.title("Attendance Module")

hello = Label(win1, text="Hello, Welcome to sensdence").pack()

choose_sub = Label(win1, text="Choose subject:").pack()

variable = StringVar(win1)
variable.set("Operating system") # default value
w = OptionMenu(win1, variable, "Operating system", "Data structures", "Physics", "Discrete mathematics", "Database Management", "Partial Differential Equations",
               "Economics", "Management", "Business, Entrepreneurship and Management","Electronics").pack()

button1= Button(win1, text="view attendance", command = onclick_view ).pack()
button2 = Button(win1, text="mark attendance", command = onclick_mark ).pack()

win1.mainloop()

