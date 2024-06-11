def sum_squares(lst):
    
    return sum([int(x**2) for x in lst])


if __name__ == '__main__':
    print(sum_squares([1, 2, 3]))
