num=int(input("Enter number :"))
cnt=0
while (num>0):
    rem=num%10
    cnt=cnt+1
    num=num//10
print(cnt)

