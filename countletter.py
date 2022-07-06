x = raw_input("enter a letter:-")
file = open("/home/administrator/Documents/python/day2/edisenkara2.text").read()
y = file.split()
count = 0
for i in y:
    for j in i:
        if j == x:
           count += 1

print(count)
