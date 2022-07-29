def doubles(n):
    """this function doubles integers"""
    return n * n


n = doubles(2)
while n < 7:
    d = doubles(n)
    n += 1
    print(d)