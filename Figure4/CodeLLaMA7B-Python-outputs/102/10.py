def choose_num(x, y):
    
    # your code here
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    for i in range(x, y + 1, 2):
        if i % 2 == 0:
            return i
    return -1


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(1, 3) == -1
    assert choose_num(2, 4) == 2
    assert choose_num(6, 9) == 8
    assert choose_num(10, 10) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
