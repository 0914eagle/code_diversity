def sum_squares(lst):
    
    # Solution 1
    # return sum([pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x for i, x in enumerate(lst)])
    
    # Solution 2
    # return sum(pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x for i, x in enumerate(lst))
    
    # Solution 3
    # return sum(map(lambda x: pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x, lst))
    
    # Solution 4
    return sum(map(lambda x: pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x, enumerate(lst)))


if __name__ == "__main__":
    print(sum_squares([1, 2, 3]))
    print(sum_squares([]))
    print(sum_squares([-1, -5, 2, -1, -5]))
