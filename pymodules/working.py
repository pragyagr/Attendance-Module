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
    subject = variable.get()
    
    def getvalue():

        #showing attendance of each student from selected dates

        E1_data = v1.get()
        E2_data = v2.get()
        print E1_data
        print E2_data

        col_list=[]
        v1_index = list.index(E1_data)
        v2_index = list.index(E2_data)
        print v1_index
        print v2_index
        if v1_index<v2_index:
            col_list = list[v1_index:v2_index+1]
        else:
            col_list = list[v2_index:v1_index+1]
        
        print col_list
        print len(col_list)
        
        cur.execute("SELECT Roll_Number, Name, %s FROM %s"  %((', '.join(col_list)),subject))
        result_set = cur.fetchall()
        for row in result_set:
            print "%d, %s," % (row[0], row[1])
            for num in range(len(col_list)):
                print "%d," %(row[num+2])
                

        '''import Tkinter
        root = Tkinter.Tk(  )
        for r in result_set:
            for c in range(2+len(col_list)):
                Tkinter.Label(root, text='Row[%ss]'%(c),borderwidth=1 ).grid(row=r,column=c)
        root.mainloop(  )'''
        
    win1.destroy()
    
    win2=Tk()
    win2.title("Attendance Module")
    win2.geometry('250x250')

    v1 = StringVar()
    v2 = StringVar()
    v1.set("mm/dd/yy")
    v2.set("mm/dd/yy")

    #date:2.12.14 . by:Pragya. for dropdownlist of "to" and "from"
    cur = db.cursor()
    cur.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA= 'student' and TABLE_NAME = '%s'" %subject)
    a = cur.fetchall()
    list = []
    for i in range(2, len(a)):
        list.append(a[i][0])
    if list:
        L = Label(win2, text="Subject: %s" %variable.get() ).pack()    
        L2= Label(win2, text="From:").pack()
        from_option = OptionMenu(win2, v1,*list).pack()
        L3= Label(win2, text="To:").pack()
        to_option = OptionMenu(win2, v2, *list).pack()
        button3 = Button(win2, text="OK", command = getvalue ).pack()
    else:
        L = Label(win2, text="There is no attendance to view").pack()

    win2.mainloop()

def onclick_mark():
    subject = variable.get()
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    date = time.strftime("%x")
    cur.execute("SHOW COLUMNS FROM `%s` LIKE '%s'" %(subject,date)) # code for adding column when it doesn't exist 
    exist = cur.fetchone()                                      # code for adding column when it doesn't exist 
    if exist is None:                                           # code for adding column when it doesn't exist 
        cur.execute("ALTER TABLE `%s` ADD `%s` INT(2) NOT NULL DEFAULT '0'" %(subject,date))    
    
    def onclick_next():
        try:
            v3_value = int(v3.get())
        except:
            error_msg = 'number you entered is not an integer'
            label_err = Label (win3, text=error_msg, fg='red').pack()
            
        try:
            err1 = "Trying...", device
            lab1 = Label(win3, text=err1).pack()
            arduino = serial.Serial(device, 9600)
            flag = 1
        except:
            err2 = "Failed to connect on ", device
            lab2 = Label(win3, text = err2).pack()
            flag = 0
        
        def attendance():
            def nextstudent():
                tempwin.destroy()
                attendance()
            tempwin = Tk()
            cur = db.cursor()
            nextstudent_button = Button(tempwin, text ="Next Student", command= nextstudent).pack()
            flag = 1
            if flag==1:
                #try:
                print "place finger assshole"
                my_id = arduino.readline()   #read the data from arduino
                print "here"
                if my_id != -2:
                    #try:
                    cur.execute("SELECT Name FROM student_att WHERE Id=%d" %(int(my_id)))
                    name = cur.fetchone()
                    print name
                    text_student = "Identified!",name
                    label_studentname = Label(tempwin, text= text_student).pack()
                    cur.execute("UPDATE `%s` SET `%s`= %d WHERE Roll_Number=(SELECT Roll_Number FROM student_att WHERE Id= %d)" %(subject, date,v3_value, int(my_id)))
                    flag = 1
##                        except:
##                            err3 = 'Failed to read from arduino. Try burning the code to arduino again'
##                            lab3 = Label(win3, text = err3).pack() 
##                except:
##                    err4 = "Failed to get data from Arduino!"
##                    print 'error', sys.exc_info()[0]      
##                    lab4 = Label(win3, text = err4).pack()
            db.commit()
            
        attendance()
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
variable.set("Operating systems") # default value
w = OptionMenu(win1, variable, "Operating systems", "Data structures", "Physics", "Discrete mathematics", "Database Management", "Partial Differential Equations",
               "Economics", "Management", "Business, Entrepreneurship and Management","Electronics").pack()

button1= Button(win1, text="view attendance", command = onclick_view ).pack()
button2 = Button(win1, text="mark attendance", command = onclick_mark ).pack()

win1.mainloop()

