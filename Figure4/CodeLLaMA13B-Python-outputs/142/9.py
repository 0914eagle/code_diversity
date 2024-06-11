def sum_squares(lst):
    
    # Solution
    return sum([pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x for i, x in enumerate(lst)])


if __name__ == '__main__':
    # Test Cases
    lst = [1, 2, 3]
    print(sum_squares(lst))

    lst = []
    print(sum_squares(lst))

    lst = [-1, -5, 2, -1, -5]
    print(sum_squares(lst))
