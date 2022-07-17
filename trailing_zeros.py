'''
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
'''

from math import factorial, log


def zeros(n):
    count = 0
    fact = lambda x: 1 if x == 1 else x * fact(x - 1)
    for i in str(factorial(n))[::-1]:
        if i == '0':
            count += 1
        else:
            break
    return count


def zeros2(n):
    result = 0
    if n > 0:
        for i in range(1, int(log((n), 5)) + 1):
            result += n // (5 ** i)
        return result
    else:
        return 0


num = 10000
print(zeros(num))
print(zeros2(num))
