#Task 2
# Given a string of text, print the number of times each letter in the alphabets a-z appear.
# Hint: “a” != “A”. eg. Given "the quick brown fox jumps over the lazy dog",
# the expected output is "a: 1, b: 1, c: 1, d: 1, e: 3 ......"

#abcdefghijklmnopqrstuvwxyz

#text = (input('Enter text')).lower()
#alphabet = list('abcdefghijklmnopqrstuvwxyz')
#string_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13,'o':14,'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
#letter_counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
#
#for i in text:
#
#	letter_counter[string_dict[i]] += 1
#
#for i in range (0, 26):
#
#	print(alphabet[i] + ': ' + str(letter_counter[i]) + '; ')

#sentence = 'The quick brown fox jumps over the lazy dog'.lower()
sentence = 'The quick brown fox jumps over the lazy dog'
#sentence_lower = sentence.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#for i  in alphabet:
#    print(i, ': ', sentence.count(i))

for i in alphabet:
    count = 0
    for j in sentence:
        if j.lower() == i:
            count +=1

    print(i, ': ', count)
