s = [1, 2, 3, 4, 5, 1, 3, 6, 2, 5, 10, 7, 8, 7, 4, 5]
odd = 0
even = 0
for i in s:
    if i % 2 == 0:
        even = even+i

    else:
        odd = odd+i

print(odd)
print(even)