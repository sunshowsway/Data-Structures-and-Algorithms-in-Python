def intify(s, n):
    if n == 0:
        return 0
    return int(s[-n]) * 10**(n-1) + intify(s, n-1)


"""
    return 1 * 10^4 + 2345 = 12345
intify("12345", 5)
    return 2 * 10^3 + 345 = 2345
intify("12345", 4)
    return 3 * 10^2 + 45 = 345
intify("12345", 3)
    return 4 * 10^1 + 5 = 45
intify("12345", 2)
    return 5 * 10^0 + 0 = 5
intify("12345", 1)
    return 0
intify("12345", 0)
"""