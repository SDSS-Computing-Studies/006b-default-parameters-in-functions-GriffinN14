#!python3

import assignment
def tempConversion(degrees, unit=("C")):
    if unit == ("C"):
        f = (degrees * 9 / 5) + 32
        f = round(f,1)
        return f
    else:
        c = (degrees - 32) * 5 / 9
        c = round(c,1)
        return c
