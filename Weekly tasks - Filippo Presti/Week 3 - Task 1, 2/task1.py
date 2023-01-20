//second input/parameter optional
def greet(given_name, family_name = False):

    greetings = 'Hello ' + given_name + '.'

    if family_name:

        greetings = 'Hello there, '+ given_name + ' of ' + family_name + '!'

    return greetings

print(greet(input('Enter your Given Name: '), input('Enter your Family Name: ')))


//def greet(given_name, family_name = ""):

//	if family_name = "":

//		print("Hello " + family_name)

//	else:

//		print('Hello there, '+ given_name + ' of ' + family_name + '!')