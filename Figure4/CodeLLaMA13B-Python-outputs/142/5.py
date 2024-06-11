def sum_squares(lst):
    
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            lst[i] = lst[i] ** 3
        sum += lst[i]
    return sum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sum_squares([]) == 0, "1st example"
    assert sum_squares([1, 2, 3]) == 14, "1st example"
    assert sum_squares([-1,-5,2,-1,-5]) == -126, "1st example"
    assert sum_squares([2,2,2,2,2]) == 60, "1st example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
