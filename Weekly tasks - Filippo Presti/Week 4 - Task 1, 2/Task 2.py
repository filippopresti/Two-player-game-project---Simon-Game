#Start with 4 words “comfortable”, “round”, “support”, “machinery”, return a list of all possible 2 word combinations.
#Example: ["comfortable round", "comfortable support", "comfortable machinery", .....]
words_list = ['comfortable', 'round', 'support', 'machinery']
new_list = []

#In case the task did not admit repetition: comfortable round = round comfortable
#for i in range(0,len(words_list)):
#    for j in range (i+1, len(words_list)):
#        new_list.append(words_list[i] + ' ' + words_list[j])
#
#print(new_list)

#In case the task did admit the use repetition: comfortable round != round comfortable
for i in range(0,len(words_list)):
    for j in range (0, len(words_list)):
        if (words_list[i] == words_list[j]):
            pass
        else:
            new_list.append(words_list[i] + ' ' + words_list[j])

print(new_list)

Teacher's version
for i in words_list:
    for j in words_list:
        if i != j:
         print(i + " " + j)
