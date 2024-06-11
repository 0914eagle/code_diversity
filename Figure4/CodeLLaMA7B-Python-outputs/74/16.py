def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    # my solution
    # return lst1 if len(lst1) > len(lst2) else lst2

    # solution 1
    return lst1 if sum([len(i) for i in lst1]) > sum([len(i) for i in lst2]) else lst2

    # solution 2
    return lst1 if sum(len(i) for i in lst1) > sum(len(i) for i in lst2) else lst2

    # solution 3
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 4
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 5
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 6
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 7
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 8
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 9
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 10
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 11
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 12
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 13
    return lst1 if sum(map(len, lst1)) > sum(map(len, lst2)) else lst2

    # solution 14
    return lst1 if sum