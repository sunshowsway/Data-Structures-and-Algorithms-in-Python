def empty_stack(S):
    if S.is_empty():
        return
    S.pop()
    return empty_stack(S)

"""
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
[1, 2, 3]
[1, 2]
[1]
[]
"""