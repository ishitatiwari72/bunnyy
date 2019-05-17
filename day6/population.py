# -*- coding: utf-8 -*-
"""
Created on Tue May 14 05:23:12 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 


    Refer to population.csv


"""
import csv
list1=[]
dic={}
f1=open('population.csv','rt')
r = csv.reader(f1, delimiter=',')
next(r)
for line in r:
    list1.append(line)
for item in list1:
    country='india'
    item[2]=item[2].replace(",","")
    dic[(country,item[3])]=int(dic.get([(country,item[3])],0))+int (item[2])

list2=[]
for line in list1:
    list2.append((line[-2],line[-1]))
def state(x):
        if x[-1]=='tamilnadu':
            return x
u=list(filter(state,list2))