def parse_int(string):
    dif_num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }
    num_rank = {
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000
    }

    num_str = string.replace('-', ' ').split()
    razr = 3
    result = 0
    pre_result = 0
    counter = 0
    for word in num_str:
        if word in dif_num_dict:
            pre_result += dif_num_dict[word]
        elif counter >= 1 and word in num_rank:
            result += pre_result
            result *= num_rank[word]
            pre_result = 0
            counter = 0
        elif word in num_rank:
            pre_result *= num_rank[word]
            result += pre_result
            pre_result = 0
            counter += 1
        if len(str(result)) > razr and counter > 0:
            counter = 0
            razr += 3
    result += pre_result
    return result


print(parse_int('one'))
print(parse_int('twenty'))
print(parse_int('two hundred forty-six'))
print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
print(parse_int('one thousand three hundred and thirty seven'))
