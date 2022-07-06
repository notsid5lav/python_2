path = "/home/administrator/Documents/python/day2/edisenkara2.text"
fill=open(path).read()
y=fill.split()
sum=0
for i in y:
    x=len(i)
    sum=sum+x
print(sum)