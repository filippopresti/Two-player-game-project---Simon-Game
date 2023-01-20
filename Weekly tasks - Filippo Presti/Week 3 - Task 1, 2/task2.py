#Function that turns any English Word into Pig Latin
#def pigLatin(word):
#    word = word.lower()
#    first_letter = word[0]
#    rest_of_word = word[1:]
#    word_lenght = len(word)
#    vowels = 'aeiou'
#    consonants = 'bcdfghjklmnpqrstvwxyz'
#
#    if word[0] in vowels:
#        pig_latin_word = word.capitalize() + 'yay'
#
#    elif word_lenght >= 3 and word[0] in consonants and word[1] in consonants and word[2] in consonants:
#        first_letter = word[0] + word[1] + word[2]
#        rest_of_word = word[3:]
#        pig_latin_word = rest_of_word + first_letter + 'ay '
#
#    elif word_lenght >= 2 and word[0] in consonants and word[1] in consonants:
#        first_letter = word[0] + word[1]
#        rest_of_word = word[2:]
#        pig_latin_word = rest_of_word + first_letter + 'ay '
#
#    else:
#        pig_latin_word = rest_of_word.capitalize() + first_letter + 'ay'
#
#    return(pig_latin_word)
#
#print(pigLatin(input("Enter the English word to be translated in Pig Latin: ")))

#teacher's version

first_word = 'string'
second_word = 'omelet'
vowel = 'aeiou'

def pig_latin(word):

    if word[0] in vowel:
        #starts with vowel
        return word + 'yay'
    else:
        #starts with consonant
        word_consonant = ''
        i = 0
        for letter in word:
            if letter in vowel:
                #letter is a vowel
                break
            else:
                #letter is a consonant
                word_consonant += letter

            i += 1
        end_string = word[i:]
        return end_string + word_consonant + 'ay'
        #print(end_string)
        #return word[i:] + word[0:i] + 'ay'

print(pig_latin(first_word))
print(pig_latin(second_word))

#Function that turns any sentence into Pig Latin
#def pigLatin(sentence):
#    sentence = sentence.lower()
#    words = sentence.split()
#    pig_latin_sentence = 'The sentence in Pig Latin is: '
#
#    for word in words:
#        word_lenght = len(word)
#        print(word_lenght)
#        if word[0] in 'aeiou':
#            pig_latin_sentence += word + 'yay '
#
#        elif word_lenght >= 3 and word[0] in 'bcdfghjklmnpqrstvwxyz' and word[1] in 'bcdfghjklmnpqrstvwxyz' and word[2] in 'bcdfghjklmnpqrstvwxyz':
#            first_letter = word[0] + word[1] + word[2]
#            rest_of_word = word[3:]
#            pig_latin_sentence += rest_of_word + first_letter + 'ay '
#
#        elif word_lenght >= 2 and word[0] in 'bcdfghjklmnpqrstvwxyz' and word[1] in 'bcdfghjklmnpqrstvwxyz':
#            first_letter = word[0] + word[1]
#            rest_of_word = word[2:]
#            pig_latin_sentence += rest_of_word + first_letter + 'ay '
#
#        else:
#            first_letter = word[0]
#            rest_of_word = word[1:]
#            pig_latin_sentence += rest_of_word + first_letter + 'ay '
#
#    return pig_latin_sentence
#
#print(pigLatin(input("Enter the sentence to be translated in Pig Latin: ")))
