# -*- coding: utf-8 -*-
"""
Created on Wed May  8 05:51:16 2019

@author: HP
"""
"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

i=0
while i<=100:
    if i%3==0 and i%5!=0 :
        print("Fizz")
        i=i+1
        
        
    elif i%5==0 and i%3!=0:
        print("Buzz")
        i=i+1
        
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
        i=i+1
    
    else:
        print(i)
        i=i+1