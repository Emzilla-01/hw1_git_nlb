# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:53:15 2020
Python DB part 2
Assignment 7.2


1. BIRDS

In the following list each number represents a type of bird.  The bird with majority wins.  In case there is a tie, the bird with a lower numeral value wins.

Ex. 
D = [1,2,3,1,4,5,6,2]

Winner is 1

@author: Emy
"""
from collections import Counter

def birds(lst, debug=False):
    _c = Counter()
    for bird_type in lst:
        _c[bird_type]+=1
    # print(_c)
    most_birds = _c[0]
    for it in _c.items():
        bird_type=it[0]
        if _c[bird_type]>_c[most_birds]:
            if debug:
                print(f"bird '{bird_type}' count '{_c[bird_type]}' gt most_birds '{most_birds}' count:'{_c[most_birds]}'")
            most_birds = bird_type
        if _c[bird_type]==_c[most_birds]:
            if bird_type < most_birds:
                if debug:
                    print(f"bird_type '{bird_type}' lt most_birds '{most_birds}'")
                most_birds = bird_type
    return(most_birds)

    
D = [1,2,3,1,4,5,6,2]
assert birds(D) == 1
print(f"birds(D)=={birds(D)}")
E = [9,9,9,8,8,8]
assert birds(E) == 8
print(f"birds([9,9,9,8,8,8])=={birds(E)}")
F = [2,3,4,2,3,4]
assert birds(F) == 2
print(f"birds([2,3,4,2,3,4])=={birds(F)}")

# =============================================================================
"""
2. LOOPS?
Write a program to display the following 
1
12
123
1234
12345 #first outer loop counts to stop
2
23
234
2345 # each outer loop increments start by 1
3
34
345
4
45
5
"""

def loopy(start, stop):
    if start >= stop:
        return()
    
    for n0 in range(start, stop+1):
        i=stop+1
        print(''.join([str(p) for p in range(n0,i)]))
        
    loopy(start+1, stop)

loopy(1,5)