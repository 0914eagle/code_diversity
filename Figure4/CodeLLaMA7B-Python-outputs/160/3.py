def do_algebra(operator, operand):
    
    return eval(''.join(map(str, operator + operand)))


if __name__ == '__main__':
    print("Example:")
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['-', '+', '*'], [2, 3, 4, 5]) == 12
    assert do_algebra(['-', '+', '*'], [1, 2, 3, 4, 5]) == 12
    assert do_algebra(['*', '+', '*'], [2, 3, 4, 5]) == 24
    assert do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120
    assert do_algebra(['*', '*', '*'], [1, 2, 3, 4, 5]) == 120
    assert do_algebra(['*', '*', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 960000
    print("Coding complete? Click 'Check' to earn cool rewards!")
