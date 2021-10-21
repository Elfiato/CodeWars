def solution(string: str, markers: list):
    result = ''
    strings_mas = string.split('\n')
    flag = False
    for st in strings_mas:
        new_st = st
        for i in st:
            if i in markers:
                    st = st[:st.index(i)-1 ]
                    flag = True
                    break
        if flag and strings_mas.index(new_st) != len(strings_mas) - 1:
            result += st + '\n'
        else:
            result += st
    return result


def solution1(string: str, markers: list):
    result = ''
    start = 0
    stop = 0
    counter = 0
    flag = False
    for letters in string:
        if letters in markers and not flag:
            if counter == 0:
                stop = counter
            else:
                stop = counter - 1
            result += string[start:stop]
            flag = True
        if letters == '\n':
            if not flag:
                stop = counter
                result += string[start:stop] + '\n'
                start = stop + 1
            else:
                result += '\n'
                start = counter+1
                flag = False
        counter += 1
    if start <= counter and not flag:
        result += string[start:counter]
    return result


def solution2(string, markers):
    '''
    best solution
    '''
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


k = (solution1('apples\noranges\ncherries pears oranges cherries pears\n, watermelons cherries @\n=', ['?', '!', '@']))
k1 = (solution("a #b\nc\nd $e f g", ["#", "$"]))
k2 = (solution('a\no s ? @ c s\n. bananas', ['.', "'", '-', ',', '?']))
k3 = solution1('\n', ['.', "'", '-', ',', '?'])
k4 = solution1('- lemons apples watermelons\nwatermelons cherries # pears\napples\noranges watermelons apples bananas', ['-', '^', '.', "'", '#', '?'])

