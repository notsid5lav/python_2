def cumul(n):

    y=[]
    count = 1
    for i in n:
        count = count * i
        y.append(count)

    print(y)

cumul([1, 2, 3, 4])