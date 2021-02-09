def transfer(D, Q):
    while not D.is_empty():
        Q.enqueue(D.delete_first())
    while not Q.is_empty():
        D.add_last(Q.dequeue())