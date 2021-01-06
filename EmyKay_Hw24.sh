# HDFS Command
# Assignment 24

# HDFS COMMAND PRACTICS
# Please note down each command you used for each problem. This assignment can be your own cheat sheet in the future.
# 1.	Create a directory /user/hadoop2 in HDFS 
hadoop fs -mkdir -p /user/hadoop2/

# 2.	Creates a file of zero length at specified location with current time as the timestamp of that.

hadoop fs -touchz /user/hadoop2/"$(date +'%H-%M')"


# 3.	Run HDFS command to delete a “temp” directory.

hadoop fs -rm -r /temp/


# 4.	List all the files/directories for the given hdfs destination path.

hadoop fs -ls /


# 5.	Command that will list the directories in /hadoop folder.

hadoop fs -ls /hadoop/


# 6.	Command to list recursively all files in hadoop directory and all subdirectories in hadoop directory

hadoop fs -ls _R /hadoop/


# 7.	List all the files inside /user/hadoop2 directory which starts with 'dir'.

hadoop fs -ls /user/hadoop2/dir*


# 8.	Create a temp.txt file. Copies this file from local file system to HDFS
touch temp.txt
hadoop fs -put temp.txt /


# 9.	Copies the file from HDFS to local file system.
hadoop fs -get /temp.txt


# 10.	Command to copy from local directory with the source being restricted to a local file reference.

hadoop fs -copyFromLocal temp.txt /

# 11.	Command to copies to local directory with the source being restricted to a local file reference.

hadoop fs -copyToLocal /temp.txt


# 12.	Command to move from local directory source to Hadoop directory.

hadoop fs -moveFromLocal temp.txt /


# 13.	Deletes the directory and any content under it recursively.

hadoop fs -rm -R /foo


# 14.	List the files and show Format file sizes in a human-readable fashion.

hadoop fs -ls -h /


# 15.	List all the files matching the pattern.

hadoop fs -ls -h /*.txt


hadoop fs -ls / | grep '.txt'



# 16.	Take a source file and outputs the file in text format on the terminal.

hadoop fs -cat /temp.txt


# 17.	Display the content of the HDFS file test on your /user/hadoop2 directory.

hadoop fs -test -d /temp0/anaconda_win
echo $?


# 18.	Append the content of a local file test1 to a hdfs file test2.

hadoop fs -appendToFile test1 /test2

# 19.	Show the capacity, free and used space of the filesystem

hadoop fs -df  /


# 20.	Shows the capacity, free and used space of the filesystem.  Add parameter Formats the sizes of files in a human-readable fashion.

hadoop fs -df -h /

hadoop fs -ls -R -h /

# 21.	Show the amount of space, in bytes, used by the files that match the specified file pattern.

hadoop fs -du /*.txt


# 22.	Show the amount of space, in bytes, used by the files that match the specified file pattern. Formats the sizes of files in a human-readable fashion.

hadoop fs -du -h /*.txt

# 23.	Check the health of the Hadoop file system.

hdfs fsck /

# 24.	Command to turn off the safemode of NameNode.

hdfs dfsadmin -safemode leave

# 25.	Format the NameNode.  

hdfs namenode -format