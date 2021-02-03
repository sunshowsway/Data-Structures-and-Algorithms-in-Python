import time

print("k = 0")
for N in (100, 1_000, 10_000, 100_000, 1_000_000):
    data = [None] * N
    start = time.time()
    for i in range(N):
        data.pop(0)
    delta = (time.time() - start) / N * 100_000
    print("N = {0:8d}; Time Taken = {1:.3f}".format(N, delta) )

print("--------")
   
print("k = n // 2")
for N in (100, 1_000, 10_000, 100_000, 1_000_000):
    data = [None] * N
    start = time.time()
    for i in range(N):
        data.pop((len(data)//2))
    delta = (time.time() - start) / N * 100_000
    print("N = {0:8d}; Time Taken = {1:.3f}".format(N, delta) )

print("--------")

print("k = n")
for N in (100, 1_00, 10_000, 100_000, 1_000_000):
    data = [None] * N
    start = time.time()
    for i in range(N):
        data.pop(-1)
    delta = (time.time() - start) / N * 100_000
    print("N = {0:8d}; Time Taken = {1:.3f}".format(N, delta) )
    
"""
k = 0
N =    10000; Time Taken = 0.073
N =   100000; Time Taken = 0.847
N =  1000000; Time Taken = 9.191
--------
k = n // 2
N =    10000; Time Taken = 0.041
N =   100000; Time Taken = 0.394
N =  1000000; Time Taken = 4.408
--------
k = n
N =    10000; Time Taken = 0.009
N =   100000; Time Taken = 0.009
N =  1000000; Time Taken = 0.009
"""
