#1)	Define a Class in Python with example 

class Pet():
    def __init__(self, name):
        self.name=name
    def say_name(self):
        print(f"Hello, my name is {self.name}")

class Doggy(Pet):
    def __init__(self, name):
        self.name=name
        self.sound="w00f"
    def speak(self):
        print(self.sound)
        
T=Doggy("Toby")
T.speak()

#2) What are Classes vs Instances 
"""Lines 3, 9 define the class:             #class Doggy(Pet):...
line 16 is an instantiation of the class    #T=Doggy("Toby")
"""

#3) How to Define a Class 

class ClassName():
    def __init__(self, *attributes):
        self.attribute = attribute
    def class_method(self):
        pass

#4) Instantiate an Object in Python 
x = 0

#5) Explain Class and Instance Attributes 
"""Per question 1, all instances of Pet will have the attribute Pet.name (class attribute).
However, T.name=="Toby" is the name attribute of instance T"""

#6) What are Instance Methods
"""Per question 1, Pet.say_name is an instance method -- it requires the class is instantiated before it is called (unlike __init__).
"""

#7) How to Inherit From Other Classes in Python 
class Wabbit(Pet):
    pass
B=Wabbit("Bugs")
B.say_name()

#8) Elaborate Parent Classes vs Child Classes 
""" The child class "Doggie" inherits attribute name and method say_name from its parent class "Pet"
"""

#9) Extend the Functionality of a Parent Class 
class Kitty(Pet):
    def __init__(self, name):
        self.sound="m30w"
        super().__init__(name) #<--- *super* keyword
    def speak(self):
        print(self.sound)
C=Kitty("Charlie")
C.say_name()

#10) What Is Object-Oriented Programming in Python?
"""designing functionality around class definitions which may be easily repurposed.
For example, let's say we are writing a script to create a sales report.

#functional approach:
def get_data(db):
    pass
def report(data):
    pass

r0=report(get_data(db))

#OOP approach:
class Report(db):
    def __init__(self):
        pass
    def get_data(self.db):
        pass
    def put_xlsx():
        pass
        
r_instance = Report(db)
r_instance.get_data()
r1 = r_instance.put_xlsx()

Although the functional approach may be faster to write, the OOP may be more portable for other solutions and may offer advantages when many changes in state must be accounted for.
"""