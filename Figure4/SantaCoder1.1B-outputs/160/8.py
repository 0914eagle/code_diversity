def do_algebra(operator, operand):
    
    # check if the length of operator is equal to the length of operand minus one
    if len(operator) != len(operand) - 1:
        raise ValueError('The length of operator list is not equal to the length of operand list minus one.')

    # build the algebra expression
    result = 0
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i]
        elif operator[i] == '-':
            result -= operand[i]
        elif operator[i] == '*':
            result *= operand[i]
        elif operator[i] == '/':
            result //= operand[i]
        elif operator[i] == '**':
            result **= operand[i]

    return result


if __name__ == '__main__':
    # test case 1
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    print(do_algebra(operator, operand))

    # test case 2
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5, 6]
    print(do