
#===================QUE 1===========================================
def fun1(name,age):
    print(f"Welcome name:{name} and age is :{age}")
#fun1('kartik',21)

name=input('enter name:')
age=input('enter age:')
print(name,age)
fun1(name, age)

#========================que2=====================================
   
def func1(a,*b):
    print(a,*b)
func1(10,20,'kartik',30)

#=====================que3=======================

def calculation(a,b):
    print('addition:',a+b,'sunstraction:',a-b)
calculation(6, 3)

#====================que4======================

def showEmployee(name,salary=9000):
    print(name,salary)
    
showEmployee('kartik', 20000)
showEmployee('Shivam')

#=====================que5=======================

def sqr(a):
    print( a**2)
calsqr=sqr
calsqr(12)

#==================que6==========================
def even(i):
    if i%2==0:
        return even
l=[i for i in range(4,30) if even(i)]
print(l)

#================que7===========================+
def uniquelist():
    l=[]
    s=int(input("enter size :"))
    for i in range(s):
        no=int(input("enter elements:"))
        l.append(no)
    print(l)
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print("Uniquelist",l1)

uniquelist()

#====================que8===================================

def sqr1():
    list_sqr=[(i,i**2) for i in range(1,31)]
    print(list_sqr)
sqr1()

#===================que9========================

l1=['r','g','b']
l2=["red","green","blue"]
d=dict(zip(l1,l2,strict=False))
print(d)

#==================Que10========================

l=[]
for i in range(11):
        num=int(input("enter element to find square:"))
        l.append(num)
l1=list(map(lambda a:a**2,l))
d=dict(zip(l,l1,strict=False))
print(d)

#==================que11=========================

x=int(input("Enter number :"))
y=int(input("Enter number :"))

a= lambda x:x+15
b= lambda x,y:x*y 
print(a(x))
print(b(x,y))

#==================que12========================

l=[]
for i in range(5):
        num=int(input("enter element to find square and cube:"))
        l.append(num)
print(l)

sqr= lambda num:num**2
cube= lambda num:num**3

l1=list(map(sqr,l))
l2=list(map(cube,l))
print("squares:", l1)
print("cube:",l2)





    