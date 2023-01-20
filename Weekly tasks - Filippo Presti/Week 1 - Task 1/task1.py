
x = input('Enter a number: ')

#if x % 2 == 0:
#   print('even')
#else:
#   print('odd')

#if x.is_integer():
#    print('int')
#else:
#   print('?');
#!!!if x = 6 you will get error but it will work if you have x as 6.0!!!
#if float(x).is_integer():
#    print('int')
    #if x % 2 == 0:
    #   print('even')
    #else:
    #   print('odd')
#else:
#   print('?');

#try except

x = float(x)
if x.isdigit() and int(x) % 2 == 0:
    print('Provided value is an even number')

elif  x.isdigit() and int(x) % 2 != 0:
    print('Provided value is an odd number')

elif x.isalnum():
    print('Provided value is neither even nor odd but a string')

else:
    print('Provided value is neither even nor odd but a float number')
