def multiply(a, b):
    
    return a % 10 * b % 10


if __name__ == '__main__':
    print("Example:")
    print(multiply(148, 412))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert multiply(148, 412) == 16
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20
    assert multiply(123, -987) == 16
    print("Coding complete? Click 'Check' to earn cool rewards!")
