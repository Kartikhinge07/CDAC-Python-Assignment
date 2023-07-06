import math
h=int(input("enter your height in cm :"))
f=h//30.48
g=h%30.48
i=math.ceil(g/2.54)
print("your height is ", f ,"feet", i ,"inch") 