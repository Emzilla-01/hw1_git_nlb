# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:43:49 2020

@author: emy
"""

billing_data = {"alan" :500,
                "laura":400,
                "meena":600}

class HighestOrderGetter():
    def __init__(self, d):
        self.data = d

    def get_highest_bill(self):
        highest = ('', 0)
        for itm in self.data.items():
            if itm[1] > highest[1]:
                highest = itm
        return(itm)

# x = HighestOrderGetter(billing_data)
# x.get_highest_bill()


# =============================================================================
# 
# =============================================================================

import mysql.connector
import os
os.system("cls")
mydb = mysql.connector.connect(host="localhost", user="root", password='', db="subway")
mycursor  = mydb.cursor()

userid = input("Enter your userid ")
password = input("Enter password ")

sql = "select * from regn where userid = '" + userid + "' and password = '" + password + "'"

mycursor.execute(sql)
data = mycursor.fetchone()
if data == None:
    print("Invalid credentials, please re-enter")
else:
    print("Welcome to SUBWAY")
    print("Password updation....")
    newp = input("Enter new password")
    rnewp = input("Re enter your new password")
    if newp != rnewp :
        n = 0
        while (n < 2):
            print("Ops! new passsword and re enter new password do not match!!  try again!")
            rnewp = input("Re enter your new password")
            n +=1
            if newp == rnewp :
                break
    else:
        sql = "update regn set password = '" + newp + "' where userid ='" + userid + "' and password ='" + password +  "'"
    
def validate_newp():
    n=0
    while n<2:
        newp = input("Enter new password")
        rnewp = input("Re enter your new password")
        if newp  == rnewp:
            return(newp)
        n+=1
        
one = 1
two = 2
print(f"one:{one}\ntwo:{two}")