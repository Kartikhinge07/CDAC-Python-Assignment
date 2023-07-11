t=[(i,i**2) for i in range(2,10)]
tu=tuple([t])
print(tu)
#----------------que2--------------------------
t="a","e","i","o","u"
tu=tuple([t])
print(tu)

#-----------------que3-------------------------

num=(2,3,4,5)
num1=(6,7,8,9)
print(num,num1,sep=" ")
print(num+num1)
t=num+num1
t2=t[::-1]
print(t2)
print(t2[2])
print(t2[-3:])
print(len(t2))

#----------------que4---------------------------

t4=("May","JUne","July","aug","sept")
t5=(123,456,789,678)
print(t4[4])
print(t5[2])

#------------------que5--------------------------
t=(1,2,5,6,3,8,5,2,1,4,6)
print(t)
num=int(input("Enter number to search:"))

print(t.count(num))

#-------------------que6---------------------------

t=(1,2,5,6,3,8,5,2,1,4,6)
print(t)
exist="false"
num=int(input("Enter number to search:"))
for i in range(0,len(t)):
    if num==t[i]:
        exist="true"
        break
    else:
        pass
if exist=="true":
    print("AVailable") 
else:
    print("not available")
