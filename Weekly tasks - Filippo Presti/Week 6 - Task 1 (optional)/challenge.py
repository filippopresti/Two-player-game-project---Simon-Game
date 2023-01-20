# binary search algorithm
a = [1, 3, 5, 7, 8]
b = 7
res = -1
new_list = []
middle = len(a) // 2
print(middle)
if a[middle] == b:
    print(a[middle])
while len(new_list) > 1:
    if middle > b:
        new_list = new_list[:middle]
    else:
        new_list = new_list[middle:]
print(new_list)