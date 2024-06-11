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
    if lst == []:
        return -1
    if len(lst) == 1:
        return -1
    if lst[0] == 0:
        return -1
    if lst[0] > 0:
        return lst[0]
    if lst[0] < 0:
        return -1
    if lst[0] > lst[1]:
        return lst[0]
    if lst[0] < lst[1]:
        return -1
    if lst[0] == lst[1]:
        return -1
    if lst[0] > lst[2]:
        return lst[0]
    if lst[0] < lst[2]:
        return -1
    if lst[0] == lst[2]:
        return -1
    if lst[0] > lst[3]:
        return lst[0]
    if lst[0] < lst[3]:
        return -1
    if lst[0] == lst[3]:
        return -1
    if lst[0] > lst[4]:
        return lst[0]
    if lst[0] < lst[4]:
        return -1
    if lst[0] == lst[4]:
        return -1
    if lst[0] > lst[5]:
        return lst[0]
    if lst[0] < lst[5]:
        return -1
    if lst[0] == lst[5]:
        return -1
    if lst[0] > lst[6]:
        return lst[0]
    if lst[0] < lst[6]:
        return -1
    if lst[0] == lst[6]:
        return -1
    if lst[0] > lst[7]:
        return lst[0]
    if lst[0] < lst[7]:
        return -1
    if lst[0] == lst[7]:
        return -1
    if lst[0] > lst[8]:
        return lst[0]
    if lst[0] < lst[8]:
        return -1
    if lst[0] == lst[8]:
        return -1
    if lst[0] > lst[