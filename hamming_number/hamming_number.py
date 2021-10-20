from itertools import islice
from time import time


def hamming(n):
    """Returns the nth hamming number"""
    hamming_nums = []
    bases = (2, 3, 5)
    queue = {1: [0, 0, 0]}
    h = 1
    while len(hamming_nums) < n:
        hamming_nums.append(min(queue))
        pows = queue[min(queue)].copy()
        del queue[min(queue)]
        for i in range(3):
            pows[i] += 1
            key = calculate_key(bases, pows)
            if queue.get(key, 0) == 0:
                queue[key] = pows.copy()
            pows[i] -= 1
        return hamming_nums[n - 1]


def calculate_key(base, power):
    result = 1
    for x, y in zip(base, power):
        result *= x ** y
    return result


def hamming2():
    """\
    This version is based on a snippet from:
        https://web.archive.org/web/20081219014725/http://dobbscodetalk.com:80
                         /index.php?option=com_content&task=view&id=913&Itemid=85
        http://www.drdobbs.com/architecture-and-design/hamming-problem/228700538
        Hamming problem
        Written by Will Ness
        December 07, 2008

        When expressed in some imaginary pseudo-C with automatic
        unlimited storage allocation and BIGNUM arithmetics, it can be
        expressed as:
            hamming = h where
              array h;
              n=0; h[0]=1; i=0; j=0; k=0;
              x2=2*h[ i ]; x3=3*h[j]; x5=5*h[k];
              repeat:
                h[++n] = min(x2,x3,x5);
                if (x2==h[n]) { x2=2*h[++i]; }
                if (x3==h[n]) { x3=3*h[++j]; }
                if (x5==h[n]) { x5=5*h[++k]; }
    """
    h = 1
    _h = [h]  # memoized
    multipliers = (2, 3, 5)
    multindeces = [0 for i in multipliers]  # index into _h for multipliers
    multvalues = [x * _h[i] for x, i in zip(multipliers, multindeces)]
    yield h
    while True:
        h = min(multvalues)
        _h.append(h)
        for (n, (v, x, i)) in enumerate(zip(multvalues, multipliers, multindeces)):
            if v == h:
                i += 1
                multindeces[n] = i
                multvalues[n] = x * _h[i]
        # cap the memoization
        mini = min(multindeces)
        if mini >= 1000:
            del _h[:mini]
            multindeces = [i - mini for i in multindeces]
        #
        yield h


def hamming3(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

def main():
    #print(int((list(islice(hamming2(), 0, 1)))[0]))
    #print(hamming(10))
    print(hamming3(10))




start_time = time()
main()
print("--- %s seconds ---" % (time() - start_time))