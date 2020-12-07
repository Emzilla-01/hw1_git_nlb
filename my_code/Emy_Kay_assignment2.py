from time import sleep

tempo = 96 #4/4 BPM
beats_per_second= tempo/60

stopwords=[r"<br>", r"</a>"]
lyrics_blob="""I bet you're wondering how I knew<br>
'Bout your plans to make me blue<br>
With some other guy you knew before<br>
Between the two of us guys<br>
You know I love you more<br>
It took me by surprise, I must say<br>
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
        
        
        
def mysum0(a,b):
    return(a+b)
mysum0(1,2)

def mysum1(*nums):
    return(sum(*nums))
mysum1([1,2])


from webbrowser import open as wb_opn
wb_opn(r"https://www.google.com/search?tbm=isch&q=%22Keanu%20Reeves%22")


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
        
import datetime        
s=r"Today is 11/22/2020"
s=s[9:]
d=datetime.datetime.strptime(s, r"%m/%d/%Y")
s1=datetime.datetime.strftime(d, r"%d %B %Y")


corpus="I bet you're wondering how I knew 'Bout your plans to make me blue With some other guy you knew before Between the two of us guys You know I love you more It took me by surprise, I must say When I found out yesterday Don't you know that I heard it through the grapevine Not much longer would you be mine Oh, I heard it through the grapevine Oh, and I'm just about to lose my mind".lower()

def simple_str_srch(corpus):
    q = str(input("please enter exact text to match corpus\n")).lower()
    m = corpus.lower().find(q)
    if m == -1:
        print("match not found")
    else:
        print(f"found query '{q}' at position {m}")
               
        
dlm = "World,Earth,America,Canada"
corpus = "Universe,Galaxy,SolarSystem,World,Earth,America,Canada,USA,Mexico,Ottawa,DC,CDMX"
lst = corpus.split(dlm)


from random import randint
x = randint(0,999)

print([randint(0,999) for i in range(3)])

lst = [randint(0,999) for i in range(100)]
count_dict = dict()
for n in lst:
    if n not in count_dict.keys():
        count_dict[n]=1
    else:
        count_dict[n]+=1

x = sorted(list(count_dict.items()), key=lambda i: i[1], reverse=True)[:10]


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
    
        

def ask_preference():
    validation_flag = False
    valid_options=["C", "JS", "PY", "PA"]
    while not validation_flag:
        i0 = input("Which do you prefer?\nenter C for COBOL\nenter JS for JavaScript\nenter PY for Python\nenter PA for Pascal...\n")
        if i0.upper() in valid_options:
            validation_flag = True
        else:
            print("This is a closed choice question.")
    return(i0.upper())
        
    

def ask_1_to_10():
    validation_flag = False
    limits=(1,10)
    while not validation_flag:
        i0 = float(input("Please select a number between 1 and 10\n"))
        if (limits[0] < i0 < limits[1]):
            validation_flag = True
        else:
            print("answer outside range")
    return(i0)
    
#Make a program that asks a password.
def ask_annoying_pw():
    rules={"length must be at least 5 characters": lambda s: len(s)>4,           
           "password must have exactly one dollar sign ($)": lambda s: s.count(r"$")==1,
           "password must have an even number of characters": lambda s: len(s)%2==0,
           "length must be less than 10 characters": lambda s: len(s)<10,
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

                
                

clist = ['Canada','USA','Mexico','Australia']
for c in clist:
    print(c)
    
    
i=0
while i<=100:
    print(i)
    i+=1
    
    
    
    
axis=list(range(1,13))
table=list()
for a in axis:
    row=list()
    for b in axis:
        row.append(a*b)
    table.append(row)
    
#two line for loop
for i in range(10,0,-1):
    print(i)
# one line listcomp
[print(i) for i in range(10,0,-1)]


[print(i) for i in range(2,11,2)]
[print(i) for i in range(1,11) if i%2==0]


l=list()
[l.append(i) for i in range(100,201)]
sum([i for i in range(100,201)])

ttl=0
for i in range(100,201):
    ttl+=i
    
    
    
clist = ["Canada","USA","Mexico"]
i=0
while i < len(clist):
    print(clist[i])
    i+=1
    
while True:
    i+=1
    i+=sum(range(1,i))
    if i>10:
        break


l=list()        
w="uWu"
while len(l) < 10:
    for c in w:
        print(c)
        l.append(c)
        
        
x=lambda l:sum(l)
x([1,2,3,4,5])


def mysum2(*nums):
    ttl=0
    for n in nums:
        ttl+=n
    return(ttl)
   
mysum2(*[1,2,3,4,5])


def foo():
    print("foo")

def bar():
    print("bar")

def foobar():
    foo()
    bar()


def rcount(c_v):
    if c_v < 10:
        c_v +=1
        print(c_v)
        return(rcount(c_v))
rcount(0)
    
def make_global():
    global x
    x = 1
make_global()
print(x)

y=[6,4,2]
more=[12,8,4]
for i in range(3):
 	y.insert(-1, x)
 	x+=4
    
y=[6,4,2]
y.insert(1,3)
y.remove(2)


x=[i for i in range(1,1001)]
max(x), min(x)


even=[i for i in range(0,21) if i%2==0]
odd =[i for i in range(0,21) if i%2!=0]


d={"US":"United States",
 "AUS": "Australia",
 "KR": "South Korea",}
for item in d.items():
    print(f"k:{item[0]}\nv:{item[1]}\n\n")
    
    


i=0
with open("arbitrary1.txt", 'rt') as textfile:
    for line in textfile:
        print(f"   {i} : {line}".lstrip())
        i+=1

with open("take_it_easy.txt", 'wt') as textfile:
    textfile.write('open("text.txt")')
    
    
axis=list(range(1,4))
table=list()
i=0
for a in axis:
    row=list()
    for b in axis:
        row.append(i)
        i+=1
    table.append(row)
    
from itertools import combinations
persons = [ “John”, “Marissa”, “Pete”, “Dayton” ]
meetings = combinations(persons,2)
[m for m in meetings]