def arithmetic_arranger(list_string, a = False):
    length = len(list_string)
    list_longest = []
    list_final = [[], [], [], []]
    # Rule 1
    if length > 5:
        return 'Error: Too many problems.'
    # }
    for i in list_string:
        first, subtract, second = i.split()
        # Rule 2 {
        if subtract != '+' and subtract != '-':
            return '''Error: Operator must be '+' or '-'.'''
        # }
        # Rule 3 {
        try:
            int(first)
            int(second)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        # }
        # Rule 4 {
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # }
        list_longest += [max(len(first), len(second))]
        # Add first, second element, and the result of add or subs to final list
        list_final[0] += [first]
        list_final[1] += [subtract + (' '*(list_longest[-1] + 1 - len(second))) + second]
        list_final[2] += ['-' * (list_longest[-1] + 2)]
        list_final[3] += [str(eval(i))]

    if not a:
        list_final.pop()

    # print(list_final)
    text = ''
    for i in list_final:
        for j in range(len(i)):
            length_i = len(i[j])
            width = list_longest[j] + 2
            text += '{}{}'.format(' '*(width - length_i), i[j])
            if j != len(i) - 1:
                text += '    '
        if i != list_final[-1]:
            text += '\n'
    return text


# For testing
# n = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
# print(arithmetic_arranger(n, True))
