def choose_num(x, y):
    
    # your code here
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    for i in range(x, y + 1, 2):
        if i >= y:
            return -1
        return i


if __name__ == '__main__':
    print("Example:")
    print(choose_num(12, 15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert choose_num(12, 15) == 14
    assert choose_num(13, 12) == -1
    assert choose_num(10, 10) == 10
    assert choose_num(10, 20) == 10
    assert choose_num(20, 20) == -1
    assert choose_num(20, 10) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
