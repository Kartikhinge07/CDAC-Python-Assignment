no1=input('enter no1 : ')
no2=input('enter no2 : ')
no3=input('enter no3 : ')

if no1>no2:
	if no1>no3:
		print(no1,'is greater')
	else:
		print(no3,'is greater')
elif no2>no3:
	print(no2,'is greater')
else:
	print(no3,'is greater')
