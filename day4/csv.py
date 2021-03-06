# -*- coding: utf-8 -*-
"""
Created on Sat May 11 06:28:26 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Reading and Writing CSV
  Filename: 
    csv.py
  Problem Statement:
    Create a program that reads from one CSV file (/etc/passwd), 
    and writes to another one. 
    
    You are to read from passwd file,
    and produce a file whose contents are the username (index 0) 
    and the user ID (index 2).
    Note that a record may contain a comment, 
    in which it will not have anything at index 2; 
    you should take that into consideration when writing the file.  
    The output file should use TAB characters to separate the elements.
 
    Thus, the input will look like:
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    _ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
    
    and the output will look like:
 
        root    0
        daemon  1
        _ftp    98
    
"""



    
import csv
dic={}
list1=[]
with open("passwd.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for line in csv_reader:
        list1.append(line.split(":"))
    for row in list1:
        for item in row:
           if dic[item[0][0]]=="#"
               pass
           dic[row[0]]=row[2]
            
print(dic)