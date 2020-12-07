# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:39:49 2020

@author: emmam
"""

# #connection
# conn = mysql.connect(host='localhost', port = 3306, user = 'root', password='', db='subway')
# #cursor  = internal pointer to the data
# mycursor = conn.cursor()
# #SQL commands can be now executed using the  cursor
# mycursor.execute("select * from yourorder")
# mydata = mycursor.fetchall()
# print(mydata)
# conn.close()
# # 

from os import system

import pymysql as mysql
system("cls")

# db = mysql.connect('localhost', 'root', password='', db='morning_12-1-2020')
db = mysql.connect('localhost', 'root', password='', db='stores_12-3-20')
cursor = db.cursor()
# cursor.execute("SELECT * from stores")
# data=cursor.fetchall()
# cursor.execute("select * from stores")

data = cursor.execute("select max(storeid) from stores")
data = cursor.fetchone()

i=data[0]
if i == None:
    i = 1
else:
    i = data[0] + 1
        
data1 = (i, input("Enter store name\n"))
cursor.execute(f"insert into stores (storeId, storename) values ({data1[0]}, '{data1[1]}')")
db.commit()
print(f"inserted {data1}")
db.close()