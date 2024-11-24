import itertools as it
import random

iterator_1 = it.cycle(range(0, 2))
for i in range(10):
    print(next(iterator_1)) # 0 1 0 1 0 1...


the_list = ["N", "E", "S", "W"]
iterator_2 = iter(lambda: random.choice(the_list), None) 
for i in range(10):
    print(next(iterator_2)) # losowo N lub E lub S lub W


iterator_3 = it.cycle(range(0, 7))
for i in range(10):
    print(next(iterator_3)) # 0 1 2 3 4 5 6 0 1 2 3 4 5 6 0 1 2...
