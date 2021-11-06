import random
import timeit
from math import gcd
from functools import reduce


def solution6(a):
    '''
    лучшее решение
    '''
    return reduce(gcd, a) * len(a)


def solution5(a):
    '''
    через множества
    '''
    a_len = len(a)
    a = set(a)
    while len(a) != 1:
        b = max(a)
        a.remove(b)
        a.add(b-max(a))
    return max(a) * a_len



def solution2(arr):
    '''
    brute force
    '''
    N = len(arr)
    end = False
    while not end:
        arr = sorted(arr, reverse=True)
        end = True
        for i in range(1, N):
            while arr[i-1] > arr[i]:
                arr[i-1] -= arr[i]
                end = False
    return sum(arr)


def solution1(arr):
    '''
    слишком долго
    '''
    arr_len = len(arr)
    if arr_len > 1:
        mn = arr[0]
        current_min_index = -1
        for i in range(0, arr_len):
            if i == current_min_index:
                return arr_len * mn
            if arr[i] == 1:
                return arr_len
            if arr[i] < mn:
                current_min_index = i
                mn = arr[i]
            if arr[i] > mn:
                dev = arr[i] % mn
                if dev != 0:
                    arr[i] = dev
                    mn = dev
                    current_min_index = i
                else:
                    arr[i] = mn
    else:
        return sum(arr)


def solution(arr):
    '''
    мое решение, которое прошло по времени
    '''
    arr_len = len(arr)
    flag = True
    if arr_len == 1:
        return arr[0]
    m = min(arr)
    k = 0
    while flag:
        for i in range(arr_len):
            if arr[i] != m:
                if arr[i] % m != 0:
                    arr[i] = arr[i] % m
                    if arr[i] < m:
                        k = i
                        m = arr[i]
                elif arr[i] % m == 0:
                    arr[i] = m
            if arr[i] == 1:
                return arr_len
        if arr[k] == arr[0]:
            flag = False
    return m * arr_len



arr1 = [random.randint(561, 5004564567) for _ in range(100000)]  # GCD will be 4 or a multiple of 4
#arr1 = [50, 16, 13]

#arr1 = [4739840, 5350835, 2439360, 2627660, 5134115, 3651515, 2685515, 171500, 3628940, 2152640, 8506715, 3385235]


#print(solution(arr1))
#print(solution2(list(arr1)))
#print(solution4(arr1))

#print(arr1)

#print(solution(arr1) == solution4(arr1))

print(timeit.timeit(lambda: solution(list(arr1)), number=1))
#print(timeit.timeit(lambda: solution2(list(arr1)), number=1))
#print(timeit.timeit(lambda: solution5(list(arr1)), number=1))
print(timeit.timeit(lambda: solution6(list(arr1)), number=1))