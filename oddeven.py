s = [1, 2, 3, 4, 5, 1, 3, 6, 2, 5, 10, 7, 8, 7, 4, 5]
odd = 0
even = 0
for i in s:
    if i % 2 == 0:
        even = even+1
    else:
        odd = odd+1

print("the number of odd values are :", odd)
print ("the number of even values are :", even)