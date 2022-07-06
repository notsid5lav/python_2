s = [1, 2, 3, 4, 5, 1, 3, 6, 2, 5, 10, 7, 8, 7, 4, 5]  # list with duplicate values
r = []  # empty list

for i in s:         #delcare a loop and check if conditon in for
    if i not in r:  #condition to check wether it is true or not
       r.append(i)

print(r)

