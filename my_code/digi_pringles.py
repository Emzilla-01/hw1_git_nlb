#EmyKay PythonQuiz
# =============================================================================
def digi_pringles(names):
    vowels = "aeiou"
    result = dict()
    for _N in names:
        count=0
        _n = _N.lower()
        for _v in vowels:
            count+=_n.count(_v)
        result[_N]=count
    return(result)

#################
"""
Write a program to find the length of the last word in a sentence.

For example:

msg = "This is a book"

should return 4
"""
def parser(sentence_str):
    sentence_lst = sentence_str.split()
    return(len(sentence_lst[-1]))
#

# =============================================================================
class Phone():
    def __init__(self, color, status="Good"):
        self.color=color
        self.status=status
    def call(self, recipient):
        print("Phone can make calls")
        print(f"dialing {recipient}")
    def sendMsg(self, recipient, msg):
        print("Phone can send msg")
        print(f"texting {recipient}: {msg}")

class IntermediatePhone(Phone):
    def __init__(self, color, status="Good", brand='generic'):
        self.brand=brand
        super().__init__(color, status)
    def fix(self):
        self.status="good" # capitalization is different per prompt requirements
        

class iPhone(IntermediatePhone):
    def __init__(self, color, status="Good", brand="Apple"):
        super().__init__(color, status, brand)




class Samsung(IntermediatePhone):
    def __init__(self, color, status="Good", brand="Samsung"):
        super().__init__(color, status, brand)
    def notePen(self):
        print("Samsung Note has a pen and Apple doesn't!")

def main():
    # =============================================================================
    my_phone = Phone('blk')
    my_phone.color, my_phone.status
    my_phone.call('Emy')
    my_phone.sendMsg('Emy', "Hello!")
    # =============================================================================
    my_iphone = iPhone("rose gold")
    my_iphone.status = 'broken screeeen'
    my_iphone.fix()
    my_iphone.brand
    # =============================================================================
    my_samsung= Samsung("silver")
    my_samsung.status="broken headphone port"
    my_samsung.fix()
    my_samsung.brand
    my_samsung.call("my_iphone")
    my_samsung.notePen()    


if __name__ == '__main__':
    main()