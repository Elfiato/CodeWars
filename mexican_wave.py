'''
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
'''

from string import punctuation


def wave1(people):
    result = []
    for i in range(len(people)):
        if people[i] not in punctuation and people[i] != ' ':
            result.append(people[:i] + people[i].upper() + people[i + 1:])
    return result


def wave(people):
    return [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if people[i].isalpha()]


print(*wave('hello'), sep=' ')
