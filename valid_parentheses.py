'''
https://www.codewars.com/kata/52774a314c2333f0a7000688
'''


def valid_parentheses(string):
    counter = 0
    open = 0
    for s in string:
        if counter == 0 and open == 0 and s == ')':
            return False
        if s == '(':
            counter += 1
            open += 1
        if s == ')' and open > 0:
            counter -= 1
            open -= 1
    if counter == 0:
        return True
    else:
        return False


print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses('hi())('))
print(valid_parentheses("(())((()())())"))
