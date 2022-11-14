def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd2(a, b):
    # if b == 0:
    #     return a
    # return gcd2(b, a % b)
    return a if b == 0 else gcd2(b, a % b)


print(gcd(12, 4))
print(gcd2(30, 5))
