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
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return -1
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return -1
        else:
            return lst[0]
    lst.sort()
    for i in range(len(lst)):
        if lst[i] > 0:
            if lst.count(lst[i]) >= lst[i]:
                return lst[i]
    return -1


print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))
