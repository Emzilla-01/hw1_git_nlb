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

I am not so comfortable in decorators and understanding the syntax of how to apply.
Not sure on motivation either- I guess decorators can be a way to modify calls to libraries while making explicit those changes in local script?'
@author: EmyKay
"""
from dateutil.relativedelta import relativedelta
import datetime
import functools

units=10**6

class Employee():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = self.get_age(age)
        self.phone = phone      
    def get_age(self, age):
        
        return(age)


class FullTimeEmp(Employee):
    def __init__(self, name, age, phone, deptno):
        self.deptno=deptno
        super().__init__(name, age, phone)

# =============================================================================
def try_decorator(o_func):
    def wrapper(*args, **kwargs):
        print(f"in wrapper")
                
        try:
            o_func(*args, **kwargs)
        except Exception as e:
            print(f"{e}, {type(e)}, in {__name__}")
            # return(f"{e}, {type(e)}, in {__name__}")
            
        return o_func(*args, **kwargs)
    return wrapper

t = lambda t: try_decorator(t)
t1=t(Exception('fail'))

class ContractEmployee(Employee):
    @try_decorator
    def __init__(self, name, age, phone, no_of_months):
        
        super().__init__(name, age, phone)
        try:
            self.age = relativedelta(datetime.datetime.now(),
                             datetime.datetime.strptime(age, "%Y-%m-%d")).years
        except ValueError as e:
            self.age=age
        self.no_of_months=no_of_months

emp3 = ContractEmployee("Emzilla", '1989-07-01', 71.76*units, 15)
emp4 = ContractEmployee("Wanton Wonton", 'wrong column', 71.76*units, 15)
dir(emp3)
emp3.no_of_months

# =============================================================================
# Decorator functionality is not completed.
# =============================================================================
# age = relativedelta(datetime.datetime.now(),
#                          datetime.datetime.strptime('1900-07-01', "%Y-%m-%d")).years
# =============================================================================
if __name__ == "__main__":        
    emp1=Employee("Uttam the Bomb", 33, 99.99*units)
    emp1.age
    emp2 = FullTimeEmp("Dongli Strongly", 25, 111.11*units, 'Engineering')
    emp2.deptno
    emp3 = ContractEmployee("Emzilla", '1989-07-01', 77.76*units, 15)
    emp3.no_of_months    
    [print(rs) for (rs) in [emp1.age, emp2.deptno, emp3.no_of_months]]
    