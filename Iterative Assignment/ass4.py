num=int(input("Enter number :"))
ori_num=num
rev=0
while (num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)
if ori_num==rev:
    print("NUMBER IS PELINDROME")
else:
    print("NOT A PELINDROME")
