#!python3

list = []
def factorPair(a,b):
    for i in range(a):
        if i > 1:
            if a / i == int(a / i):
                list.append(i)
    return list
