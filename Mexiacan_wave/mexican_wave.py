def wave(people):
    return [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if people[i].isalpha()]


print(*wave('hello'), sep=' ')
