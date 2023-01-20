# Task 1
#Given 3 positive integers, find the sum of all numbers between the first two that are a multiple of the third.
# eg. Given "1, 10, 2", the expected output is "20" (2+4+6+8=20).

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
n3 = int(input('Enter third number'))
n_swap = 0
total = 0

if n1 > n2:
	n_swap = n1
	n1 = n2
	n2 = n_swap

for i in range (n1, n2):
	#for i in range (n1, n2+1): if you want to include second value itself
	if i % n3 == 0:
		total += i;



print(total)
