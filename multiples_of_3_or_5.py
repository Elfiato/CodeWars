'''
https://www.codewars.com/kata/514b92a657cdc65150000006
'''


def solution(number):
    res_sum = 0
    for num in range(3, number):
        if num % 3 == 0 or num % 5 == 0:
            res_sum += num
    return res_sum


print(solution())
