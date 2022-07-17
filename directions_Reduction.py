'''
https://www.codewars.com/kata/550f22f4d758534c1100025a
'''


def dirReduc(arr):
    i = 0
    d = [('NORTH', 'SOUTH'), ('SOUTH', 'NORTH'), ('EAST', 'WEST'), ('WEST', 'EAST')]
    count = 0
    while True:
        while i <= len(arr) - 2:
            if (arr[i], arr[i + 1]) in d:
                del arr[i]
                del arr[i]
                count += 1
                continue
            i += 1
        if count == 0:
            break
        count = 0
        i = 0
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"])
