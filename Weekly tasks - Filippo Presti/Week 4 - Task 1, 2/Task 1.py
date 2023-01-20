#Write a program that given a list of numbers, multiply all numbers in the list.
#Bonus for ignoring non-number element. Example: input: [1, 2, 3, 4], output: 24

#numbers = [1, 2, 3, 4, 1, 1, 10]
#total = 1
#
#for i in numbers:
#    total = total * i
# OR total *= i
#
#print(total)

#OR

#numbers = [1, 2, 3, 4]
#total = 1
#for i in range(0,len(numbers)):
#    total = total * numbers[i]
#
#print(total)

#BONUS
numbers = ['mission', 2, 3, 4, 'love','free', 10]
#numbers = ['mission','love','free']

def multiply_my_list(list):
    total = 1
    if all(isinstance(item, str) for item in numbers):
        total = 0
    else:
        for i in list:
            if type(i) == str:
                #total = total
                pass
            else:
                total = total * i
    return total

print(multiply_my_list(numbers))
