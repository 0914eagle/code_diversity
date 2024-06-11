def do_algebra(operator, operand):
    
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '*', '*', '+'], [2, 3, 4, 5]) == 23
    assert do_algebra(['+', '*', '*', '+', '+', '*'], [2, 3, 4, 5, 6, 7]) == 239
    assert do_algebra(['+', '*', '*', '+', '+', '*', '+', '*', '*'], [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2398
    assert do_algebra(['+', '*', '*', '+', '+', '*', '+', '*', '*', '+'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 23981
    print("Coding complete? Click 'Check' to earn cool rewards!")
