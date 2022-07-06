def cumul(n):
    y = []
    count = 1
    for i in n:
        count = count * i
        y.append(count)
    return (y)


def cumul2(lis):
    val = cumul(lis)
    print(val)


cumul2([1, 2, 3, 4, 5])
