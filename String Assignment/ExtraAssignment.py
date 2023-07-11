# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:04:12 2023

@author: KARTIK
"""
#================que1 ==========================

s="This is a python the language"
l=s.split(" ")
for i in l:
    if (len(i)%2==0):
        print(str(i),end=" ")
        
#=============== que 2========================
s="hello world am kartik"
a=s.split()
res=[]

for i in a:
    x=i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res=" ".join(res)
print(res)
#-------------------------------------------
l = s.split()
l1 = []

for i in l:
    str1 = ""
    for j in range(0,len(i)):
        if j == 0 or j == len(i)-1:
            str1 = str1 + i[j].upper()
        else:
            str1 = str1 + i[j]
    l1.append(str1)

s2 = " ".join(l1)
print(s2)
    
        
#================que 3=======================

s="welcome2ourcountry34"
flag1=False
flag2=False

for i in s:
    if (i.isalpha()):
        flag1=True
    elif(i.isdigit()):
        flag2=True
if(flag1==True and flag2==True):
    print("True")
else:
    print("False")
   

#================= que 4===================

s = "wweelllcccooo"
l = list(s)
print(l)
d = dict.fromkeys(l)
for i in range(0,len(s)):
    cnt = 0
    for j in range(0,len(s)):
        if s[i] == s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})
l = []
for i in d.values():
    l.append(i)
m = min(l)

l1 = []
for i in d.keys():
    if d[i] == m:
        l1.append(i)
print(l1) 
        
#==================que 5=========================

s = "wweelllcccooo"
l = list(s)
print(l)
d = dict.fromkeys(l)
for i in range(0,len(s)):
    cnt = 0
    for j in range(0,len(s)):
        if s[i] == s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})
l = []
for i in d.values():
    l.append(i)
m = max(l)

l1 = []
for i in d.keys():
    if d[i] == m:
        l1.append(i)
        
print(l1) 

#================== que 6========================

s = "wweelllcccooo"
l = list(s)
print(l)
d = dict.fromkeys(l)
for i in range(0,len(s)):
    cnt = 0
    for j in range(0,len(s)):
        if s[i] == s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})

l1 = []
for i in d.keys():
    if d[i]%2== 1:
        l1.append(i)
        
print(l1)

#=================== que 7=======================
s="geeksforgeeks is best for geeks"
ch_list=['e','b','g','f']
d={}
d2={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
for i in d:
    for j in range(len(ch_list)):
        if i==ch_list[j]:
            d2[i]=d[i]

print(d2)

#=================== que 8================================

mySubject = "Computer Science"

print(mySubject[0:len(mySubject)])
print(mySubject[-7:-1])
print(mySubject[::2])
print(mySubject[len(mySubject)-1])
print(2 * mySubject)
print(mySubject[::-2])
print(mySubject[:3] + mySubject[3:])
print(mySubject.swapcase())
print(mySubject.startswith('Comp'))
print(mySubject.isalpha())

#+=================== que 9 ===========================
myAddress = "WZ-1, New Ganga Nagar, New Delhi"

print(myAddress.lower())
print(myAddress.upper())
print(myAddress.count('New'))
print(myAddress.find('New'))
print(myAddress.rfind('New'))
print(myAddress.split(','))
print(myAddress.split(' '))
print(myAddress.replace('New', 'Old'))
print(myAddress.partition(','))
print(myAddress.index('Ganga'))


#Q10---------------------------------------------------------------------------

line=input("Enter the line : ")

total_char=len(line)
print("Total no.of characters - ",total_char)

alpha,digit,symbol1,space=0,0,0,0
for i in line:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
        

for i in line:
    if (i.isdigit()==False and i.isalpha()==False and i.isspace()==False):
        symbol1+=1
        
line=line.split(" ")
print("Total no.of words - ",len(line))

print("Total no.of alphabets - ",alpha)
print("Total no.of digits - ",digit)
print("Total no.of symbols - ",symbol1)
print("Total no.of spaces - ",space)




      
    
    
    
