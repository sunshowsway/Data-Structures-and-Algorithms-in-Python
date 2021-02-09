def transfer(D, S):
    while not D.is_empty():
        S.push(D.delete_first())
    while not S.is_empty():
        D.add_first(S.pop())