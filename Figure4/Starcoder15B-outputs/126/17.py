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
    # if len(lst) == 1:
    #     return True
    # if len(lst) == 2:
    #     return lst[0] < lst[1]
    # if len(lst) == 3:
    #     return lst[0] < lst[1] and lst[1] < lst[2]
    # if len(lst) == 4:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3]
    # if len(lst) == 5:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3] and lst[3] < lst[4]
    # if len(lst) == 6:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3] and lst[3] < lst[4] and lst[4] < lst[5]
    # if len(lst) == 7:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3] and lst[3] < lst[4] and lst[4] < lst[5] and lst[5] < lst[6]
    # if len(lst) == 8:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3] and lst[3] < lst[4] and lst[4] < lst[5] and lst[5] < lst[6] and lst[6] < lst[7]
    # if len(lst) == 9:
    #     return lst[0] < lst[1] and lst[1] < lst[2] and lst[2] < lst[3] and lst[3] < lst[4] and lst[4] < lst[5] and lst[5] < lst[6] and lst[6] < lst[7] and lst[7] < lst[8]
    # if len(lst) == 10:
    #     return lst[0] < lst[1