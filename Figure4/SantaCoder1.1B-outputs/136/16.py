def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    if len(lst) == 0:
        return (None, None)
    if len(lst) == 1:
        return (lst[0], lst[0])
    if len(lst) == 2:
        if lst[0] < 0 and lst[1] > 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0:
            return (lst[0], lst[1])
        else:
            return (None, None)
    if len(lst) == 3:
        if lst[0] < 0 and lst[1] > 0 and lst[2] > 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0 and lst[2] < 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0 and lst[2] > 0:
            return (lst[0], lst[2])
        elif lst[0] < 0 and lst[1] > 0 and lst[2] < 0:
            return (lst[1], lst[2])
        else:
            return (None, None)
    if len(lst) == 4:
        if lst[0] < 0 and lst[1] > 0 and lst[2] > 0 and lst[3] > 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0 and lst[2] < 0 and lst[3] < 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0 and lst[2] > 0 and lst[3] < 0:
            return (lst[0], lst[2])
        elif lst[0] < 0 and lst[1] > 0 and lst[2] < 0 and lst[3] > 0:
            return (lst[1], lst[3])
        elif lst[0] < 0 and lst[1] > 0 and lst[2] > 0 and lst[3] < 0:
            return (lst