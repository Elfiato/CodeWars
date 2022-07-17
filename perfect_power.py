'''
https://www.codewars.com/kata/54d4c8b08776e4ad92000835
'''

import time
from math import log, floor, sqrt


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(f'время выполнения {(time.perf_counter_ns() - start_time) / (10 ** 9)} c')
        return res

    return wrapped


@time_of_function
def isPP2(n):
    for i in range(2, n + 1):
        k = round(log(n, i), 15)
        if k % int(k) == 0 and int(k) != 1:
            return [i, int(k)]


def isPP1(n):
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i ** j == n:
                return [i, j]
            if j ** i == n:
                return [j, i]


def isPP(n):
    for i in range(2, n + 1):
        k = int(round(log(n, i)))
        if i ** k == n:
            return [i, k]


@time_of_function
def main():
    for i in range(100):
        print(isPP(125))
        print(isPP(216))
        print(isPP(3241792))
        print(isPP(4))
        print(isPP(9))
        print(isPP(5))
        print(isPP(484))
        print(isPP(232))
        print(isPP(100))
        print(isPP(216))


main()
