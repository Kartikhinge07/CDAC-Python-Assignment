#que1---------------------------------

s="An enhanced Interactive Python"
s.replace('a','$')

#que2--------------------------------------

s="An enhanced Interactive Python"
n=12
str=""
for ch in range(0,len(s)):
    if (ch!=n):
        str=str+s[ch]
print(str)

#que3-----------------------------------

s="aeiouuuughtyrh"
v="a,e,i,o,u"
cnt=0
for ch in s:
    #if ch.isalpha():
        if ch in v :
            cnt=cnt+1
print(cnt)

#que4-----------------------------------

s="An enhanced Interactive Python"
s.replace(" ", "-")

#que5-----------------------------------

s="An enhanced Interactive Python"
cnt=0
for ch in s:
    cnt=cnt+1
print(cnt)

#que6----------------------------------

s="An enhanced Interactive Python"
str=""
for ch in range(0,len(s)):
    if (ch%2!=0):
        str=str+s[ch]
print(str)

#que7---------------------------------

s="An enhanced Interactive Python"
cnt=0
cnt2=0
for i in s:
    if(i.isupper()):
        cnt=cnt+1

    if(i.islower()):
        cnt2=cnt2+1
print(cnt ,"Upper case")
print(cnt2,"lower case")

#que8----------------------------------

s="asdfghjkjhgfdsa"
str=""
str=s[::-1]
if s==str:
    print(str)
    print("STRING IS PELINDROME")
else:
    print("NOT PELINDROME")

#que9----------------------------------

s="My Name is Kartik"
str=""
str=s[0:2]+s[-2]+s[-1]
print(str)

#que10----------------------------------

str1=input("ENTER A STRING:")
s=input("CHAR to check in string Starting with:")
if (str1.startswith(s)):
    print("AVAILABLE")
else:
    print("not available")
    
#que11----------------------------------

s="aeiouuuumbnvldkpfopghtyrh"
v="a,e,i,o,u"
cnt=0
for ch in s:
    #if ch.isalpha():
        if ch not in v :
            cnt=cnt+1
print(cnt)

#que12------------------------------------
name=input("Enter name:")
age=int(input("Enter age:"))
salary=int(input("Enter Salary:"))
#---DEFAULT POSITION---------
#print("Hello, my name is {} age {} and getting salary {}".format(name,age,salary))

#-----POSITIONAL FORMATTING---------

#print("Hello, my name is {0} age {1} and getting salary {2}".format(name,age,salary))

#-----KEY VALUE FORMATTING----------

#print("Hello, my name is {n} age {a} and getting salary {s}".format(n=name,a=age,s=salary))  

#-------F-Function-------------------
print(F"Hello, my name is {name} age {age} and getting salary {salary}")

#que13-----------------------------------------

s="AlwaysThinkposiTive"
len(s)
s[5]

s[8:5:-1]

s[::-1]


#que14--------------------------------------

s="The Quick brown fox jumps over the lazy dOG"
print(s)
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.capitalize())

#que15---------------------------------------

str=input("ENTER STRING TO COUNT ALPHABET:")
cnt=0
for ch in str:
    cnt=cnt+1
print(cnt)

#que16--------------------------------------

s="An enhanced Interactive Python234"
sum=0
for ch in s:
    if ch.isdigit()==True:
        z=int(ch)
        sum=sum+z
print(sum)

#que17-------------------------------------

str=input("Enter String:")
lst=str.split()
for i in lst:
    if "a" in i:
        print(i)

#que18----------------------------------------
s='clever'
for i in range(0,len(s)):
    for j in range(i+1):
        print(s[j],end=" ")
    print()

#que19------------------------------------------

s="string slicing in python"
str=s.split()
for i in str:
    print(i[0:2],end=" ")
    
    