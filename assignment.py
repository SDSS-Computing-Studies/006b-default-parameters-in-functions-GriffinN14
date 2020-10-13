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
    list.append(int(a/b))
    list.append(b)
    list.sort()
    return list


def cosineLaw(a,b,c,oppositeSide=True):
    if oppositeSide == True:
        answer = math.cos(toRadians(c))
        return answer

def convertAngle():
    pass

def solution(a,b):
    pass

def quadratic(a,b,c):
    list = [1,2]
    d = (math.sqrt(b*b - 4 * a * c) + (b-b*2)) / (2 * a)
    e = (math.sqrt(b*b - 4 * a * c) - (b-b*2)) / (2 * a)
    list[0] = d
    list[1] = e
    list.sort
    return list

def toRadians(a):
    rad = a * math.pi / 180
    return rad