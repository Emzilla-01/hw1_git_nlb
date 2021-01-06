import os

#from logging import 
def log():
    pass

calls = [
          # 1)  Create a directory /hadoop/hdfs in HDFS
          'hadoop fs -mkdir -p /hadoop/hdfs', 

          # 2) Command to copy from local directory with the source being restricted to a local file reference. (Use copyFromLocal)
          'hadoop fs -copyFromLocal $(ls *.txt) /hadoop/',

          # 3)  Command to copies to local directory with the source being restricted to$          
          'hadoop fs -copyToLocal /hadoop/newfile.txt',

          # 4) Command to move from local directory source to Hadoop directory.
          'hadoop fs -moveFromLocal $(ls *.txt) /hadoop/',
          
          #5) Create a Python script to read the data from newfile.txt filename 
          'hadoop fs -cat /hadoop/newfile.txt', # no.5 appears below os.system calls
          
          #6) Create python Script to delete empty directory 
          'hadoop fs -rmdir /hadoop/hdfs',
          
          #7) Deletes the directory and any content under it recursively.
          'hadoop fs -rm -R /hadoop',

        ]

results = list()

[ (print("\ncall {} system.('{}')".format(calls.index(c)+1 ,c)),
    results.append( ( c , os.system(c) ) )) for c in calls]


for r in results:
    print('{} : {}\n'.format(r[0],r[1]))


