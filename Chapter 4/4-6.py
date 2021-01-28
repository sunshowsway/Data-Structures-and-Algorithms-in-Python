def harmonic(n):
    if n == 1:
        return 1
    return 1/n + harmonic(n-1)


"""
    return 1/5 + 1/4 + 1/3 + 1/2 + 1
harmonic(5)
    return 1/4 + 1/3 + 1/2 + 1
harmonic(4)
    return 1/3 + 1/2 + 1
harmonic(3)
    return 1/2 + 1 
harmonic(2)
    return 1
harmonic(1)
"""