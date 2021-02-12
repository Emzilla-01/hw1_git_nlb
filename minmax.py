# call like "python3 minmax.py '/output/part-r-00000'"


from sys import argv
import subprocess
import re
import datetime
#import pandas as pd # afraid to install python3-pip due to some instability in vm image
#import numpy as np

if __name__ == '__main__':

    r = r'[0-9]+'
    if 0:
            with open(argv[1], 'rt') as textfile:
                    l = [line for line in textfile.readlines()]
                    rl = [re.findall(r, i) for i in l]

    call = "hadoop fs -cat {}".format(argv[1])

    rl = subprocess.check_output(call, shell=True)
    rl= rl.decode().split("\n")
    rl = [re.findall(r, i) for i in rl]

    MIN = None
    MAX = None


    i0=0
    for line in rl:
            if line == []:
                            continue
            t = float(line[1]) + float(line[2])*.1
            d = datetime.datetime.strptime(line[0], "%Y%m%d")
            if i0 == 0:
                    #init MIN,MAX
                    MIN = (i0, t, d)
                    MAX = (i0, t, d)
            #compare
            if t < MIN[1]:
                    MIN = (i0, t, d)
            if t > MAX[1]:
                    MAX = (i0, t, d)
            i0+=1

    print("\nColdest day: {}\nTemp: {}c\n".format(str(MIN[2])[:11], MIN[1]))
    print("\nWarmest day: {}\nTemp: {}c\n".format(str(MAX[2])[:11], MAX[1]))

