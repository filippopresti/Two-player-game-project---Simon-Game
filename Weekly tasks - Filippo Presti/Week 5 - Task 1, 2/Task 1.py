#task 1
#Make a program that uses a lookup table to convert any set of alphabets into their corresponding NATO phonetic alphabets.
#Also implement the inverse function.
#- Input: cat
#- Output: charlie alfa tango

nato_alphabet =  {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}
given_word = input('Enter word to convert: ')

def convert_nato(input):
    nato_word =''
    for i in input.upper():
        for j in nato_alphabet:
            if i == j:
                nato_word += nato_alphabet.get(j) + ' '
            else:
                pass
    return(nato_word)

print(convert_nato(given_word))

#implementation

given_nato_word = (input("Enter a sentence in NATO alphabet: ")).lower()
word_list = given_nato_word.split()
decoded_word = ''
for word in word_list:
    for nato_word in nato_alphabet.values():
        if word == nato_word.lower():
            decoded_word += nato_word[0]


print(decoded_word.capitalize())


#without using dictionaries

#given_nato_word = (input("enter a sentence ")).lower()
#word_list = given_nato_word.split()
#decoded_word = ''
#for word in word_list:
#    decoded_word += word[0]
#
#print(decoded_word.capitalize())


#teacher vesrion
nato = [' ' : ' ','a' : 'alfa' ...]
def word_to_nato(word):
    result = ''
    for letter in word:
        print letter
        result += nato[letter]

    print('result')


word_to_nato('cat')

#implementation

def nato_to_word(sentence):
    for word in sentence.split():
        for key, value in nato.items():
            if value == word:
                print(key)

        print(word)

nato_to_word('charlie alpha tango')
