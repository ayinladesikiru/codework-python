import math

r = [2, 4, 7, 8, 3]


def area(r):
    return math.pi * r


print(list(map(area, r)))

