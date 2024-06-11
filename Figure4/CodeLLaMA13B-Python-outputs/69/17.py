def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # your code here
    max_freq = 0
    max_num = -1
    for num in lst:
        if num > max_freq:
            max_freq = num
            max_num = num
        elif num == max_freq:
            max_num = max(num, max_num)
    return max_num if max_freq >= max_num else -1


if __name__ == '__main__':
    print("Example:")
    print(search([4, 1, 2, 2, 3, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
