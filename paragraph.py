path ="/home/administrator/Documents/python/day2/edisenkara2.text"

fil = open(path).read()

y=fil.split()
for i in fil:
    if i not in y:
       y.append(i)

print(y)