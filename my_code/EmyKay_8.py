# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:38:29 2020

1. DATABASE SCHEMA
Write a program to demonstrate inheritance feature by creating 2 classes namely
-	fulltime_emp, and contract_emp which are derived from the parent class employee
-	employee class will have name , age, phone
-	contract_emp class will have additional deatail which is no_of_months\
    fulltime_emp class will have dept_code as additional data

Just code of accepting the data and displaying for one object each of the contract and fulltime emp


2. DECORATORS
Write a program to demonstrate the use of decorators in python. you can take your own examples 


@author: Emy
"""
class Employee():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = self.get_age(age)
        self.phone = phone      
    def get_age(self, age):
        return(age)
    
emp1=Employee("John Smith", "25", "1234567")
emp1.age

class FullTimeEmp(Employee):
    def __init__(self, name, age, phone, deptno):
        self.deptno=deptno
        super().__init__(name, age, phone)

emp2 = FullTimeEmp("Joan Doe", 45, '123561', 'Engineering')
emp2.deptno

class ContractEmployee(Employee):
    def __init__(self, name, age, phone, no_of_months):
        self.no_of_months=no_of_months
        super().__init__(name, age, phone)

emp3 = ContractEmployee("Emy Zilla", 31, "9999999", 15)
emp3.no_of_months

# =============================================================================
# Decorator functionality is not completed.
# =============================================================================
import datetime
from dateutil.relativedelta import relativedelta
import functools

def my_age_decorator(func):
    def wrapper(*args, **kwargs):
        age = func(*args, **kwargs)
        print(age)
        try:
            age = relativedelta(datetime.datetime.now(), datetime.datetime.strptime(age , "%Y-%m-%d")).years
        except Exception as e:
            print(f"{e}, {type(e)}, in {__name__}")
            
        return(func(*args, **kwargs))
    return(wrapper)
    # return(wrapper)
        

class Employee4(FullTimeEmp):
    @my_age_decorator
    def get_age(self, age):
        super().get_age(age)
    def __init__(self, name, age, phone, deptno):
        self.age=self.get_age(age)
        super().__init__(name, age, phone, deptno)
    # pass
emp4=Employee4("Emo Kay", '1989-07-21', '12345', 'eng')
emp4.name
emp4.age
    