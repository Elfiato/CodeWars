import itertools
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(f'время выполнения {time.perf_counter_ns() - start_time}')
        return res

    return wrapped


@time_of_function
def next_bigger1(n):
    # return int(''.join(sorted([i for i in str(n)], reverse=True)))
    m = tuple(str(n))
    com = sorted(set(itertools.permutations(m, len(m))))
    try:
        return int(''.join(com[com.index(m) + 1]))
    except IndexError:
        return -1


def next_bigger2(n):
    mx = n
    n = str(n)
    flag = False
    for i in range(len(n)-1, -1, -1):
        for j in range(len(n)-1, -1, -1):
            if i != j:
                if i > j:
                    k = int(f'{n[:j]}{n[i]}{n[j+1:i]}{n[j]}{n[i+1:]}')
                else:
                    k = int(f'{n[:i]}{n[j]}{n[i + 1:j]}{n[i]}{n[j+1:]}')
                if k > int(n) and not flag:
                    mx = k
                    flag = True
                if k > int(n) and flag:
                    if k < mx:
                        mx = k
    return mx if flag else -1


@time_of_function
def next_bigger(n):
    num = {}
    n = str(n)
    flag = False
    for i in range(len(n) - 1, -1, -1):
        for j in range(len(n) - (len(n) - i), -1, -1):
            if n[i] > n[j]:
                flag = True
                base = f'{n[i]}{n[j+1:i]}{n[j]}{n[i+1:]}'
                num[base] = n[:j]
                break
    if flag:
        mn = base
        for key in num:
            if int(key) < int(mn):
                mn = key
        work_part = [i for i in mn[1:]]
        return int(num[mn] + mn[0] + ''.join(sorted(work_part)))
    else:
        return -1



print(next_bigger(12))
print(next_bigger(21))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(1234567890))
print(next_bigger(22930373361))
