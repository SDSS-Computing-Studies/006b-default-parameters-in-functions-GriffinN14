#! python3

import math

def tempConversion(degrees, unit="C"):
    if unit == "C":
        f = (degrees * 9 / 5) + 32
        f = round(f,1)
        return f
    else:
        c = (degrees - 32) * 5 / 9
        c = round(c,1)
        return c


def factorPair(a,b):
    list = []
    for i in range(a):
        if i > 1:
            if a / i == int(a / i):
                list.append(i)
    return list


def cosineLaw():
    pass

def convertAngle():
    pass

def solution():
    pass

def quadratic():
    pass
