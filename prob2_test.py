import random
import time

"""
length of list starting from 10000,
size increases 10 times per iteration.
"""

record = []
size = 1000
for i in range(1, 5):
    size *= 10
    lst = [random.randint(1, 1000000000) for _ in range(size)]
    start = time.time()
    lst.sort()
    end = time.time()
    print(f"Size of list: {size}\nTime: {end-start}\n")
