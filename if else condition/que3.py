m1=int(input('enter marks m1 : '))
m2=int(input('enter marks m2 : '))
m3=int(input('enter marks m3 : '))
m4=int(input('enter marks m4 : '))
m5=int(input('enter marks m5 : '))	

per = (m1+m2+m3+m4+m5)/5
print('percentage is : ' ,per)

if per>90:
	print('Distinction')
elif per<90 and per>75:
	print('First class')
elif per<75 and per>60:
	print('second class')
elif per<60 and per>36:
	print('third class')
else:
	print('fail')