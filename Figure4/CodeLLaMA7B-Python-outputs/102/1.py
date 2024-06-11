def choose_num(x, y):
    
    # your code here
    if x % 2 != 0 or y % 2 != 0:
        return -1
    if x > y:
        return -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(100, 100) == -1
    assert choose_num(100, 101) == -1
    assert choose_num(100, 102) == 102
    print("Coding complete? Click 'Check' to earn cool rewards!")