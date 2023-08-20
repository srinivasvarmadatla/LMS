import serial
from serial import Serial
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='123456',database='library')
mycus=db.cursor()
se = serial.Serial('COM5', 9600)
line_count = 0
while True:
    
    if se.in_waiting:
        print("............")
        data = se.readline().decode('utf-8').rstrip('\n')
        line_count += 1
    
        if line_count == 2:
            parts = data.split(" ")
            x=parts[0]
            y=parts[1]
            z=parts[2]
            sql="INSERT INTO L_M_S(id,b_name,author) values(%s,%s,%s)"
            val=(x,y,z)
            mycus.execute(sql,val)
            db.commit()
            print("record inserted")
            