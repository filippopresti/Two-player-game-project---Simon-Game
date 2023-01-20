#python task1v2.py

a = input("Enter a number: ")

if a.isdigit():
	print('Provided value is an integer')

	a = int(a) % 2

	if (a==0):
		print('Provided value is an even number')
	else:
		print('Provided value is an odd number')

else:
	print('Provided value is not an integer')