# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:38:57 2020

@author: emmam
"""

##################################################
## Emy's Python refresher code
##################################################

#########################
# Em's GetVersionInfo.py
#########################
# This script will provide version for installed packages   
# use pkg_Resources module  
import pkg_resources  
from pkg_resources import get_distribution
packages=["numpy", "scipy", "scikit-learn", "statsmodels", "cv2", "sqlite3", "bs4", "nltk",]

#I was making a get_version_dict() but didn't complete all cases in time.
def print_version(pk):
    try:
        print("*"*25)
        print(f"{pk} : {get_distribution(pk)}")
    except Exception as e:
        try:
            exec(f"import {pk}")
            exec(f"print(pk + ' : '+ {pk}.__version__)")
        except Exception as e1:
            try:
                exec(f"print(pk + ' : '+ {pk}.version)")
            except Exception as e2:
                print(f"{pk} exception trying to import: {e2}, {type(e2)}\n")
                raise e2
                
if __name__ == "__main__":
    for pk in packages:
        print_version(pk)
        
r"""dev local output since monday anaconda re-installation
(base) C:\Users\emmam\Documents\nlb>python GetVersionInfo.py
*************************
numpy : numpy 1.19.2
*************************
scipy : scipy 1.5.2
*************************
scikit-learn : scikit-learn 0.23.2
*************************
statsmodels : statsmodels 0.12.0
*************************
cv2 : 4.0.1
*************************
sqlite3 : 2.6.0
*************************
bs4 : 4.9.3
*************************
nltk : nltk 3.5
"""
# 1. The version of numpy package installed on your system is:  
#  numpy 1.19.2
# 2. The version of statsmodels package installed on your system is:
#  statsmodels 0.12.0
# 3. The version of scikitlearn (sklearn) package installed on your system is:
#  scikit-learn 0.23.2
# 4. Following command provides version information for sqlite3 package
#  sqlite3.version
#5. What is the description of NLTK package in ANACONDA NAVIGATOR?
# Natural language toolkit


# 1) Make a Python program that prints your name.
"".join([chr(c) for c in [69, 109, 121, 32, 75, 97, 121]])

# 2) Make a program that displays couple lines of the lyrics of a song.
from time import sleep
tempo = 96 #4/4 time so BPM is.... variable- would need to check again
beats_per_second= tempo/60

stopwords=[r"<br>", r"</a>"]
lyrics_blob="""It took me by surprise, I must say<br>
When I found out yesterday<br>
Don't you know that
I heard it through the grapevine</a><br>
Not much longer would you be mine<br>
Oh, I heard it through the grapevine<br>
Oh, and I'm just about to lose my mind<br>"""
for sw in stopwords:
    lyrics_blob=lyrics_blob.replace(sw, "")

lyrics_blob = lyrics_blob.replace(r"<br>", "")
lyrics_blob.replace(r"</a>", "")
lyrics_lst = lyrics_blob.split("\n")

if __name__ == "__main__":
    print(lyrics_lst[0])
    for line in lyrics_lst[1:]:
        sleep(beats_per_second)
        print(line)

# • Variables
# 3) Make a program that solves and shows the summation of 64 + 32.
sum([64,32])
# 4) Make a program that solves and shows the summation of two variables.
def mysum0(a,b):
    return(a+b)

def mysum2(*nums):
    ttl=0
    for n in nums:
        ttl+=n
    return(ttl)

# 5) Make a program that displays your favorite actor/actress.
if __name__ == 0:
    from webbrowser import open as wb_opn
    wb_opn(r"https://www.google.com/search?tbm=isch&q=%22Keanu%20Reeves%22")

# 6) Try to print the word ‘lucky’ inside s.
def lucky_s():
    block="lucky"
    block_l=len(block)
    shape=[ [1,1,1],
            [1,0,0],
            [1,1,1],
            [0,0,1],
            [1,1,1],
           ]
    for line in shape:
        linebuf=''
        for cell in line:
            if cell == 1:
                linebuf+=block
            else:
                linebuf+=" "*block_l
        print(linebuf)


if __name__ == "__main__":
    try:
        lucky_s()
    except Exception as e:
        raise(ZeroDivisionError("fail"))

# 7) Try to print the day, month, year in the form “Today is 11/22/2020”.
import datetime        
s=r"Today is 11/22/2020"
s=s[9:]
d=datetime.datetime.strptime(s, r"%m/%d/%Y")
s1=datetime.datetime.strftime(d, r"%d %B %Y")
if __name__ == "__main__":
    try:
        print(d, s1)
    except Exception as e:
        raise(ZeroDivisionError("fail"))
# • String replace
# 8) Try the replace program
"hello".replace("l","1")
# 9) Can a string be replaced twice?
"hello".replace("l","1e").replace('e','3').replace("31","UwU")
# 10) Does replace only work with words or also phrases?
"you are freak".replace("freak","of nature")
# • String find
# 11) Find out if string find is case sensitive
"hello".replace("o","o world!").find("H")
# 12) What if a query string appears twice in the string?
#Only the first will be found by str.find()
"hello".find('l')==2
# 13) Write a program that asks console input and searches for a query.
def simple_str_srch(corpus):
    q = str(input("please enter exact text to match corpus\n")).lower()
    m = corpus.lower().find(q)
    if m == -1:
        print("match not found")
    else:
        print(f"found query '{q}' at position {m}")
        
if __name__ == "0":
    with open("EmyKay_python_assignment2.py", 'rt', encoding='utf-8') as textfile:
        x=str(textfile.readlines())
        simple_str_srch(x)
# • String join
# 14) Create a list of words and join them, like the example above.
"“ uWu ”".join(["“here”", "“we”", "“go”", "“!!!”"])

# 15) Try changing the separator string from a space to an underscore.
" ".replace(" ", "_").join(["snake", "case"])
# • String split
# 16) Can a string be split on multiple characters?
"hello world".split("o w")
# 17) Can you split a string this string?: World, Earth, America, Canada
dlm = "World,Earth,America,Canada"
corpus = "Universe,Galaxy,MilkyWay,SolarSystem,World,Earth,America,Canada,USA,Mexico,Ottawa,DC,CDMX"
lst = corpus.split(dlm)
# 18) Given an article, can you split it based on phrases?
"""
corpus = scrape(“https://www.archives.gov/founding-docs/declaration-transcript”) 
x = corpus.split(“He has”)
>>> x
[“The unanimous Declaration of the thirteen united States….”,
“refused his Assent to Laws…”,
“forbidden his Governors to pass Laws of immediate and pressing importance…”,
“refused to pass other Laws for the accommodation of large districts of people…”,
…]
"""
# • Random numbers
# 19) Make a program that creates a random number and stores it into x.
from random import randint
x=randint(0,999)

# 20) Make a program that prints 3 random numbers.
print([randint(0,999) for i in range(3)])

# 21) Create a program that generates 100 random numbers and find the frequency of each
# number.
from random import randint
lst = [randint(0,5) for i in range(100)]
count_dict = dict()
for n in lst:
    if n not in count_dict.keys():
        count_dict[n]=1
    else:
        count_dict[n]+=1

x = sorted(list(count_dict.items()), key=lambda i: i[1], reverse=True)[:10]
# • Keyboard input
# 22) Make a program that asks a phone number.
#should be like # import re
def validate_phone():
    from string import digits
    validation_flag = False
    min_len = 10
    max_len = 12
    while not validation_flag:
        input_phone=str(input("Please enter your phone number"))
        strip_buf=[]
        [strip_buf.append(c) for c in input_phone if c in digits]
        processed_phone="".join(strip_buf)
        if (min_len <= len(strip_buf) <= max_len):
            validation_flag = True
    return(processed_phone)

# 23) Make a program that asks the users preferred programming language.
def ask_preference():
    validation_flag = False
    valid_options=["C", "JS", "PY", "PA"]
    while not validation_flag:
        i0 = input("Which do you prefer?\nenter JS for JavaScript\nenter PY for Python\nenter PA for Pascal...\nenter C for COBOL\n")
        if i0.upper() in valid_options:
            validation_flag = True
        else:
            print("This is a closed choice question.")
    return(i0.upper())

# • If statements
# 24) Make a program that asks the number between 1 and 10. If the number is out of range the
# program should display “invalid number”.
def ask_1_to_10():
    validation_flag = False
    limits=(1,10)
    while not validation_flag:
        i0 = float(input("Please select a number *between* 1 and 10\n"))
        if (limits[0] < i0 < limits[1]):
            validation_flag = True
        else:
            print("invalid number")
    return(i0)

# 25) Make a program that asks a password.
def ask_annoying_pw():
    rules={"length must be at least 5 characters": lambda s: len(s)>4,
           "length must be less than 10 characters": lambda s: len(s)<10,
           "password must have exaclty one dollar sign ($)": lambda s: s.count(r"$")==1,
           "password must have an even number of characters": lambda s: len(s)%2==0,
           }
    validation_flag = False
    while not validation_flag:
        i0 = str(input("please enter a new password\n"))
        limit = len(rules)
        iters = 0
        rules_lst=list(rules.items())
        for r0 in rules_lst:
            truth_test = r0[1](i0)
            if not truth_test:
                print(r0[0])
                break
            iters+=1
            if truth_test and iters==limit:
                validation_flag = True
    return(i0)
# • For loops
# 26) Make a program that lists the countries in the set
clist = ['Canada','USA','Mexico','Australia']
cset ={'Japan','China','Korea','Phillipines'}
for c in clist:
    print(c)
for c in cset:
    print(c)
# 27) Create a loop that counts from 0 to 100
def hundo_loop():
    i=0
    while i<=100:
        print(i)
        i+=1
    return()

# 28) Make a multiplication table using a loop
def multiplication_table(start,stop):   
    axis=list(range(1,13))
    table=list()
    for a in axis:
        row=list()
        for b in axis:
            row.append(a*b)
        table.append(row)
    return(table)
# 29) Output the numbers 1 to 10 backwards using a loop

for i in range(10,0,-1):
    print(i) #two line for loop

[print(i) for i in range(10,0,-1)]# one line listcomp

# 30) Create a loop that counts all even numbers to 10

[print(i) for i in range(2,11,2)]#range increment by 2
[print(i) for i in range(1,11) if i%2==0]#modulo

# 31) Create a loop that sums the numbers from 100 to 200

sum([i for i in range(100,201)])#listcomp

ttl=0
for i in range(100,201): # for
    ttl+=i

# • While loops

# 32) Make a program that lists the countries in the set below using a while loop.
clist = ["Canada","USA","Mexico"]
cset = set()
i=0
while i < len(clist):
    print(clist[i])
    i+=1
# 33) What’s the difference between a while loop and a for loop?
"""
A for-loop uses the form “for item in iterable” and performs some operation at each item in that iterable. There is no (or minimal?) risk that this could result in an endless loop.

A while-loop uses the form “while condition” and checks that condition after each step until that condition is not met (or indefinitely). Care should be taken that the condition will be negated.

However, at some level, these are not completely distinct concepts… a for-loop is basically working like this:

"""
# 34) Can you sum numbers in a while loop?
"Like yield or.?"
def sum_while(limit):
    i=0
    while True:
        i+=1
        i+=sum(range(1,i))
        print(i)
        if i>limit:
            break
# 35) Can a for loop be used inside a while loop?
def for_inside_while():
    l=list()        
    w="uWu"
    while len(l) < 10:
        for c in w:
            print(c)
            l.append(c)
# • Functions
# 36) Make a function that sums the list 
mylist = [1,2,3,4,5]
mysum2(*mylist)
    
# 37) Can functions be called inside a function?
def foo():
    print("foo")
def bar():
    print("bar")
def foobar():
    foo()
    bar()
# 38) Can a function call itself? (hint: recursion)
def rcount(c_v):
    if c_v < 10:
        c_v +=1
        print(c_v)
        return(rcount(c_v))
# 39) Can variables defined in a function be used in another function? (hint: scope)
def make_global():
    global x
    x = 1

if __name__=="__main__":
    make_global()
    print(x)

# • Lists
# 40) Make a program that displays the states in the U.S.
states = [ 'Alabama', 'Maryland','Wyoming' ]
[print(s) for s in states]
# (You can assume this is the complete list of all states. As long as the code is correct
# will be fine, no need to get the exact output.)
# 41) Display all states starting with the letter M
[print(s) for s in states if s[0].upper() == "M"]

# • List operations
# 42) Given the list 
y = [6,4,2] #add the items 12, 8 and 4.
"I know there is a way to do this like y.insert(12-4)...(8-4)... but.."
for n in [12,8,4]:
 	y.append(n) 
# 43) Change the 2nd item of the list to 3.
y.insert(1,3)
y.remove(2)

# • Sorting list
# 44) Given a list with pairs, sort on the first element
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
# Now sort on the second element
sorted(sorted(x, key=lambda i0:i0[0]), key=lambda i1:i1[1])

# • Range function

# 45) Create a list of one thousand numbers
x=[i for i in range(1,1001)]
# 46) Get the largest and smallest number from that list
max(x), min(x)
# 47) Create two lists, one contains the even numbers from 0 to 20, the other one contains only
# odd numbers instead.
even=[i for i in range(0,21) if i%2==0]
odd =[i for i in range(0,21) if i%2!=0]

# • Dictionary
# 48) Make a mapping from countries to country short codes. Print each item (key and value). For
# example, US = United States
d={"US":"United States",
   "AUS": "Australia",
   "KR": "South Korea",}
for item in d.items():
    print(f"k:{item[0]}\nv:{item[1]}\n")
# • Read file
# 49) Read a file and number every line
i=0
with open("arbitrary.txt", 'rt') as textfile:
    for line in textfile:
        print(f"   {i} : {line}".lstrip())
        i+=1

# 50) Find out what the program does if the file doesn’t exist.
if 0:
    raise FileNotFoundError
# 51) What happens if you create a file with another user and try to open it?
"""
toor@LAPTOP-T50G4RTF:/mnt/c$ sudo touch 'notmyfile.txt'
[sudo] password for toor:
touch: cannot touch 'notmyfile.txt': Permission denied
"""
# • Write file
# 52) Write the text Take it easy to a file
with open("take_it_easy.txt", 'wt') as textfile:
    textfile.write("Take it easy")
# 53) Write the line open(“text.txt”) to a file
with open("take_it_easy.txt", 'wt') as textfile:
    textfile.write('open("text.txt")')

# • Nested loops
# 54) Given a tic-tac-toe board of 3x3, print every position
def tictactoe():
    axis=list(range(1,4))
    table=list()
    i=0
    for a in axis:
        row=list()
        for b in axis:
            row.append(i)
            i+=1
        table.append(row)
    return(table)

# 55) Create a program where every person meets the other
# persons = [ “John”, “Marissa”, “Pete”, “Dayton” ]
from itertools import combinations
persons = [ "John", "Marissa", "Pete", "Dayton"]
meetings = combinations(persons,2)
[m for m in meetings]

# 56) If a normal for loop finishes in n steps O(n), how many steps has a nested loop?
"""
usually O(n**2) like a multiplication table...?
but not always and not exactly.

"""

# • Slices
# 57) Take a slice of the list below:
pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana", "Diavoli"]
my_slice = (pizzas[-1])
# 58) Given the text “Hello World”, take the slice “World”
"Hello World"[6:]

# • Multiple return
# 59) Create a function that take in two numbers, and returns the variables as well as their sum
def multi_return(a,b):
    return({"a":a,
            "b":b,
            "c":a+b})
# 60) Create a class with 5 attributes. Inside the class, create a function getAttribute(), which will
# return all 5 attributes.
class jawn5():
    def __init__(self):
        self.one=1
        self.two=1
        self.three=1
        self.four=1
        self.five=1
    def getAttributes(self):
        l=[]
        for s in dir(self):
            if not callable(eval(f"self.{s}")):
                l.append(s)
        return(l)
x = jawn5()
x.getAttributes()
                
# • Scope
# 61) Suppose we have a variable ‘balance’ with a value of 100. Create a function
# reduceAmount(moneyOut), which will reduce the moneyOut amount from the variable
# balance.
class UserAccount():
    def __init__(self):
        self.balance=0
        self.userId=hash("hello")
    def reduceAmount(self, currency):
        currency=float(currency)
        assert type(currency) in [int, float]
        self.balance -= currency
    def incrementAmount(self, currency):
        currency=float(currency)
        assert type(currency) in [int, float]
        self.balance += currency

x = UserAccount()
x.incrementAmount(100)
x.reduceAmount(100)

# • Try except
# 62) Can try-except be used to catch invalid keyboard input?
def try_input():
    validationFlag=False
    while not validationFlag:
        x=input("write a $")
        try:
            assert r"$" in x
            validationFlag=True
        except AssertionError as e:
            print("$ must be given not taken")
        
# 63) Can try-except catch the error if a file can’t be opened?
FileNotFoundError, FileExistsError, '?'

# 64) When would you not use try-except?
'to fail loudly not silently'
# • Iterable
# 65) What is an iterable?
'a special kind of object inside python'
'a defined series of elements like a list, tuple, set, dict or others'
'a generator is not an iterable'
# 66) Which types of data can be used with an iterable?
'any data can be stored inside an iterable'
# OOP exercises
# • Class
# 67) Can you have more than one class in a file?
# 68) Can multiple objects be created from the same class?
class jawn6(jawn5):
    def __init__(self):
        self.six=1
        super(jawn6, self).__init__()

        
# 69) Can objects create classes?
"yes, calling dict() references calls the dictionary constructor object"
# • Getter and setter
# 70) Create a class Human with attribute name, and create a getter and a setter for name.
class Human():
    def __init__(self):
        self.name=""
    def setName(self, name_):
        self.name = name_
    def getName(self):
        return(self.name)
    @staticmethod
    def human_sum(a,b):
        return(sum([a,b]))
        
    
# 71) Why would you use getter and setter methods?
"assignment operator cannot be called in many conditions, for example inside listcomp"

# • Modules
# 72) Import the math module and call the sin function
from math import sin
from numpy import arange
[sin(i) for i in arange(0.01,0.99,.1)]
# 73) Try to create you own module, import and use the functions defined inside that module.
with open("__init__.py", 'at', encoding="utf-8") as textfile:
    pass
from os import path
path.exists("__init__.py")
from EmyKay_python_assignment2 import jawn5, jawn6

# • Static method
# 74) Can a method inside a class be called without creating an object? Create one as your
# example.
Human.human_sum(50,50)
# 75) Why does not everybody like static methods?
"Because if they don't rely on the attributes of self, why are they part of class?"
# • Classmethod
# 76) What is a classmethod?
# 77) How does a classmethod differ from a staticmethod?
#  Powered by
# • Multiple inheritance
# 78) Do all programming languages support multiple inheritance?
"nope"
# 79) Why would you not use multiple inheritance?
"parent functionality is not relevant or names / calls would become too confusing?"
https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem
https://en.wikipedia.org/wiki/C3_linearization
https://stackoverflow.com/questions/10674428/python-supports-a-limited-form-of-multiple-inheritance-in-what-way-limited
# 80) Is there a limit to the number of classes you can inherit from?
"no limit!"