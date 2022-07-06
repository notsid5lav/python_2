x = "/home/administrator/Documents/python/day2/edisenkara2.text"
fil=open(x).read()
even=0
odd=0
y=fil.split()

for i in y:
    x=len(i)
    if x % 2 == 0:
        even=even+1
    else:
        odd=odd+1

print(even)
print(odd)