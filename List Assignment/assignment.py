#----------------que1-----------------------------------

l=[1,2,3,4,5,6]
avg=sum(l)/len(l)
print(avg)

#-----------------que2------------------------------------

list=(-1,2,3,4,9,7,43,-34,-99,4,1,7,8)
neg=(i for i in list if i<0)
poseven=(i for i in list if i%2==0 and i>0)
posodd=(i for i in list if i%2==1 and i>0)
print(sum(neg),sum(poseven),sum(posodd), end="")

#----------------que3----------------------------------
l=[11,34,56,32,44,55,79,86,53,99]
even=(i for i in l if i%2==0)
odd=(i for i in l if i%2==1)

print(max(even), max(odd))

#-----------------que4--------------------------------------
list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
l=[i[0:3] for i in list]
print(l)

#-----------------que5---------------------------------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

for i in range(0,len(l)):
    print(l1[i],l.count(l1[i]))
    
#-----------------que6--------------------------------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
print(max(l))

#-----------------que7-------------------------------------

l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
print(l.sort())
print(l)
print("first largest:",max(l))
sec_large =(i for i in l if i!=max(l))
print("second Largest:" ,max(sec_large))

#----------------que8--------------------------------------

l=[11,34,56,32,44,55,79,86,53,99]
even=(i for i in l if i%2==0)
odd=(i for i in l if i%2==1)
print(even)
print(odd)

#-----------------que9--------------------------------------
l=[11,34,56,32,44,55,79,86,53,99]
l1=[11,34,32,32,44,55,79,86,11,11,34,44,79]

print(l+l1)
l1.sort()
print(l1)

#-----------------que10--------------------------------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
l[0],l[-1]=l[-1],l[0]

print(l)

#------------------que11--------------------------------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
l1=[]
print(l)
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

#------------------que12----------------------------------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
num=int(input("Enter index to find"))
list=l.index(num)
print(list)

#--------------------ALTERNATE QUE12---------------
l=[11,34,32,32,44,55,79,86,11,11,34,44,79]
num=int(input("Enter index to find"))
for i in range(0,len(l)):
    if (num==l[i]):
        print(i)
        
#-----------------que13----------------------------------------------=

num=int(input("Enter your choice from 1 to 8:"))
l=[1,2,3,4,5,5]
print("List before operation:")
print(l)
if num==1:
    val=int(input("Enter your value to add:"))
    l.append(val)
    
elif num==2:
    val=int(input("enter value to add :"))
    pos=int(input("enter on which positon to add:"))
    l.insert(pos,val)
    
elif num==3:
    delete=int(input("Enter value to delete:"))
    l.remove(delete)
elif num==4:
    delete=int(input("enter position to delete"))
    del l[delete]
    
elif num==5:
    l.sort()
    
elif num==6:
    l.sort()
    l.reverse()
elif num==7:
    l.reverse()
elif num==8:
    print(l)
else:
    print("Enter a valid number")
print(l)

#------------------que14------------------------------------------
l=[(i,i**2) for i in  range(11,21)]
print(l)

#------------------que15------------------------------------------
l=[i for i in range(1,1000) if i%7==0]
print(l)

#------------------que16----------------------------------------
list5=[i for i in range(0,1001) if '5' in str(i)]
print(list5)

#-------------------que17--------------------------------------
wordlist=["this","is","an","example"]
charlist=[i[0] for i in wordlist ]
print(charlist)

#------------------que18-------------------------

wordlist=["this","is","an","example"]
charlist=[(i,str(len(i))) for i in wordlist ]
print(charlist)