import serial
import MySQLdb
import time

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="student") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

date = time.strftime("%x")
cur.execute("ALTER TABLE attendance ADD `%s` INT(2) NOT NULL DEFAULT '0'" %date)

#read id from fingerprint sensor
device = 'COM4'
flag = 0
while 1:
    if flag==0:
        try:
            print "Trying...", device
            arduino = serial.Serial(device, 9600)
            flag = 1
        except:
            print "Failed to connect on ", device
            flag = 0
    if flag==1:
        try:
            my_id = arduino.readline()   #read the data from arduino
            if my_id != -2:
                try:
                    cur.execute("UPDATE attendance SET `%s`='1' WHERE Roll_Number=(SELECT Roll_Number FROM student_att WHERE Id= %d)" %(date, int(my_id)))
                except:
                    print 'Failed to read from arduino. Try burning the code to arduino again'
        except:
            print "Failed to get data from Arduino!"
            flag = 0;
    #if my_id != -2:
        #try:
        #cur.execute("UPDATE attendance SET `%s`='1' WHERE Roll_Number=(SELECT Roll_Number FROM student_att WHERE Id= %d)" %(date, my_id))
       # except:
           # print 'Failed to read from arduino. Try burning the code to arduino again'
    db.commit()
