f="Hello hello  Hello And and esoteric ESOTERIC  "
d=[]
for i in f.split():
    f=i.upper()
    if f not in d:
        d.append(f)

print(d)