# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:44:50 2023

@author: KARTIK
"""
#==================que1======================

def division(a,b):
    return a/b
try:
    a=int(input("Enter No1 : "))
    b=int(input("Enter No2 : "))
    print(division(a, b))
except Exception as e:
    print(e)
    
#==================que2===========================
while(1):
    try:
        age = int(input("Enter age:"))
        height = float(input("Enter height:"))
        weight=float(input("Enter weight:"))
        name=input("Enter name:")
        surname=input("Enter surname:")
    except Exception as e:
        print(e)
    else:
        print("Thank you")
        break
    
#=====================que3========================
def print_list(thelist,index):
    print(thelist[index])
thelist=[1,2,3,4,5,6,7]
try:
    
    index=int(input("Enter Index:"))
    print(print_list(thelist, index))
    
except Exception as e:
    print(e)
 
#====================que5========================
class InvalidAge(Exception):
    pass
try:
    age=int(input("Enter your age:"))
    
    if age<18:
        raise InvalidAge("you are not Eligible")
    else:
        print("Eligible for voting")
except Exception as e:
    print(e)
    
#===================que6========================
lst=[1,2,3,4,5,6,7]
   
try:
    element=int(input("enter element to search:"))
    position=int(input("Enter position to check:"))
    
    if element in lst:
        print("Element Available")
        
    else:
        print("Element not available")
    if position> len(lst):
        print("positon out of range")
    else:
        print("Position available and element is :",lst[position])

except Exception as e:
        print(e)
        

