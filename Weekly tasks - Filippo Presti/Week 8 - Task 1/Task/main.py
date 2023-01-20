import sys
from Levenshtein import distance as dist
#import numpy as np


#print(dist('govarnment', 'government'))
#1
#print(dist('govarnmen', 'government'))
#2
#print(dist('govarnment', 'hello'))
#10



# words = open("words.txt").readlines()
# words = [word.strip() for word in words]
# print(words)
#
# def read_file(filename):
#     lines = []
#     with open(filename, 'r') as f:
#         for line in f:
#             lines.append(line.strip())
#     return lines
#
# print(read_file('words.txt'))


#print(words)
#print('hello' in datafromfile)
#true
#print('hello helo hello government governmetn' in words)
#true
#print('hello' in words)
#false ???


# datafromfile = np.loadtxt("words.txt", dtype="str")
# #print(datafromfile[1])
#
# real_words = np.loadtxt("real words.txt", dtype="str")
# #print(real_words)
#
# for i in datafromfile:
#     word1 = i
#     for j in real_words:
#         word2 = j
#         if dist(word1, word2) == 0:
#             print('word is spelled correctly: ' + word1 + word2)
#             #remove that word from the array
#             print(datafromfile)
#             print(datafromfile)
#         elif dist(word1, word2) >= 1:
#             print(word1, word2)


#Teacher's version
text = open('cyberspace_original.txt')
dictionary_file = open('dictionary.txt')
dictionary = dictionary_file.readlines()
lines = text.readlines()


for index, word in enumerate(dictionary):
    dictionary[index] = word.strip()

#print(dictionary)
split_lines = []


#Split into words
for line in lines:
    split_lines.append(line.split(''))
#print(split_lines)

#Spellchecking
for line in split_lines:
    for i, word in enumerate(line):
        if word.lower().strip() in dictionary or word == '\n':
            #spelled correctly
            #print(word)
            line[i] = word
        else:
            minimum = 3
            correct_word = word
            for dict_word in dictionary:
                final_distance = dist(word.lower(), dict_word)
                if minum > final_distance:
                    minum = final_distance
                    correct_word = dict_word
            print(str(minimum) + ' ' + corrected_word)
            line[i] = correct_word





#Output text
join_lines = []
for split_line in split_lines:
    join_lines.append(''.join(split_line))

with open('corrected.txt', 'w') as file:
    file.write(''.join(split_line))

print(''.join(split_line))

# input_file = ''
# output_file = ''
#
# for i, arg in enumerate(arguments):
#     if arg == '-i':
#         input_file = arguments[i+1]
#     elif arg == '-o':
#         output_file = arguments[i+1]
#
# with open(input_file, mode = 'r') as input:
#  lines = input.readlines()
#  lines = [int(line.strip()) for line in lines]
#
#  with open(output_file, mode = 'w') as output:
#      output.write(str(sum(lines)))
#  print(lines)
