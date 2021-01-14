def sum_odd_squares(n):
    sum_ = 0
    for i in range(n):
        if i % 2 == 0:
            continue
        sum_ += i * i
    return sum_