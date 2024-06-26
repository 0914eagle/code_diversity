def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # lst = [1, 2, 2, 3, 3, 4]
    # lst = [1, 2, 3, 4, 5, 6, 7]
    # lst = [1, 3, 2, 4, 5, 6, 7]
    # lst = [1, 2, 2, 3, 3, 4]
    # lst = [1, 2, 2, 2, 3, 4]
    # lst = [1, 2, 3, 4, 5]
    # lst = [1, 2, 3, 4, 5, 6]
    # lst = [1, 2, 3, 4, 5, 6, 7]
    # lst = [1, 3, 2, 4, 5, 6, 7]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # lst = [1, 2, 3, 