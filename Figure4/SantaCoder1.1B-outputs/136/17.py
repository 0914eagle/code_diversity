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
    if not lst:
        return (None, None)
    elif len(lst) == 1:
        return (lst[0], lst[0])
    elif len(lst) == 2:
        if lst[0] < 0 and lst[1] > 0:
            return (lst[0], lst[1])
        elif lst[0] > 0 and lst[1] < 0:
            return (lst[1], lst[0])
        else:
            return (None, None)
    else:
        if lst[0] < 0:
            a = largest_smallest_integers(lst[1:])
            return (a[0], lst[0])
        elif lst[1] > 0:
            b = largest_smallest_integers(lst[0:])
            return (b[1], lst[1])
        else:
            return (None, None)


