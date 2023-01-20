#task 2
#Implement a Caesar Cipher function that takes a string and shift amount, outputs the encrypted string.
#- Input: hello word
#- Shift by: 7
#- Output: olssv dvysk

#implementation
#Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
#Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
#A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
#X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W
alphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
input = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
#input = 'hello word'
shift_by = -3
#shift_by = 7
output = ''
get_position = 0
for letter in input.lower():
    if letter.isspace() == True:
        output += " "
    else:
        for position_letter, alphabet_letter in alphabet.items():
            if letter == alphabet_letter:
                get_position = int(position_letter) + shift_by
                if get_position > 26:
                    get_position -= 26
                    output += alphabet[get_position]
                elif get_position <= 0:
                    get_position += 26
                    output += alphabet[get_position]
                else:
                    output += alphabet[get_position]

print(output)

# 100%26 = 22
alphabet = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4 ...}
def caeser(word, shift):
    for letter in word:
        rotated = (alphabet[letter] + shift) % 4
        for key, value in alphabet.items():
            if rotated == value:
                print(key)
                break
        print(letter)
