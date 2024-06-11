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
    if not lst:
        return -1
    else:
        max_freq = 0
        max_num = 0
        for i in lst:
            if i > max_num:
                max_num = i
                max_freq = 1
            elif i == max_num:
                max_freq += 1
        return max_num if max_freq >= len(lst) / 2 else -1

if __name__ == '__main__':
    lst = [4, 1, 2, 2, 3, 1]
    print(search(lst))