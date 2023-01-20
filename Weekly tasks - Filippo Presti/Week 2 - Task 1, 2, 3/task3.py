#Task 3
# Implement division as a series of subtraction.
# The program should only deal with integers and report the remainder if there is one.
# eg. 10/2 => 10-2-2-2-2-2=0, 10 minus 2 five times so the division result is 5 with a remainder of 0

n1 =int(input("Enter dividend: "))
while n1<0:
    print("Dividend must be a positive number!")
    n1 = int(input("Enter dividend: "))


n2=int(input("Enter divisor: "))
while n2<0 or n2 == 0:
    print("Divisor must be a positive number and cannot be 0")
    n2= int(input("Enter divisor: "))


tot = n1
result = 0
remainder = 0


while tot > 0:
    if tot - n2 >= 0:
     tot = tot - n2 #tot -= n2
     result += 1
    else:
     remainder = tot
     tot = 0


print('The result of the division is ' + str(result) + ' with a remainder of ' + str(remainder))


first = 11
second = 2

count = 0

while first >= second:
    first -= second
    count += 1

print(count)
print(first) #this will be the remainder
