def reverse(l, S):
    i = len(l)
    for _ in range(i):
        S.push(l.pop())
    for _ in range(i):
        l.append(S.pop())