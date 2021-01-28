def max_recurse(s, n):
    if n == 1:
        return s[0]
    previous = max_recurse(s, n-1)
    current = s[n-1]
    if current > previous:
        return current
    return previous


# max_recurse is O(n) in time-complexity and O(n) in space-complexity

"""
    return 3 if 3 > 20 else 20 = 20
max_recurse([5, 10, 20, 11, 3], 5))
    return 11 if 11 > 20 else 20 = 20
max_recurse([5, 10, 20, 11, 3], 4)
    return 20 if 20 > 10 else 10 = 20
max_recurse([5, 10, 20, 11, 3], 3)
    return 10 if 10 > 5 else 5 = 10
max_recurse([5, 10, 20, 11, 3], 2)
    return 5  
max_recurse([5, 10, 20, 11, 3], 1)
"""