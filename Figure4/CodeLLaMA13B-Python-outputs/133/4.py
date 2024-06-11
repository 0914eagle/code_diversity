def sum_squares(lst):
    
    return sum([int(i**2) for i in lst])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sum_squares([1, 2, 3]) == 14, "1st example"
    assert sum_squares([1, 4, 9]) == 98, "2nd example"
    assert sum_squares([1, 3, 5, 7]) == 84, "3rd example"
    assert sum_squares([1.4, 4.2, 0]) == 29, "4th example"
    assert sum_squares([-2.4, 1, 1]) == 6, "5th example"
