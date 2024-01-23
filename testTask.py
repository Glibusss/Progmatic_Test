def ternary(num):
    base = 3
    res = ''
    while num > 0:
        res = str(num % base) + res
        num //= base
    return res


def mathExpression(k):
    ter = ternary(k)
    terList = list(ter)
    mark = [''] * 9
    for i in range(1, 10):
        t = i - 1
        i *= (-1)
        if t < len(terList):
            element = int(terList[i])
            if element == 0:
                mark[i] = ''
            elif element == 1:
                mark[i] = '+'
            elif element == 2:
                mark[i] = '-'
        else:
            mark[i] = ''
    expression = ''
    for i in range(9):
        expression += f'{9-i}{mark[i]}'
    expression += '0'
    return expression


def solution(expected):
    dictResults = {}
    quantity = 3**9
    for i in range(quantity):
        expression = mathExpression(i)
        result = eval(expression)
        if result in dictResults:
            dictResults[result].append(expression)
        else:
            dictResults[result] = [expression]
    if expected in dictResults:
        return f'Value {expected} can be obtained from expressions: {dictResults[expected]}'
    else:
        return f'No solution'


value = input('Enter integer value: ')
try:
    value = int(value)
    print(solution(value))
except ValueError:
    print('Error! Invalid input value!')


