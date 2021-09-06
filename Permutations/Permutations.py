import itertools


def permutations(string):
    result = []
    st = ''
    for i in sorted(set(itertools.permutations(string, len(string)))):
        for j in i:
            st += j
        result.append(st)
        st = ''
    return result


print(permutations('ab'))