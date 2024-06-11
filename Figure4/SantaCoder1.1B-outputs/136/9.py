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
        return None, None
    if len(lst) == 1:
        return lst[0], lst[0]
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0], lst[1]
        else:
            return lst[1], lst[0]
    if len(lst) == 3:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                return lst[0], lst[2]
            else:
                return lst[2], lst[0]
        else:
            if lst[1] > lst[2]:
                return lst[1], lst[2]
            else:
                return lst[2], lst[1]
    if len(lst) == 4:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > lst[3]:
                    return lst[0], lst[3]
                else:
                    return lst[3], lst[0]
            else:
                if lst[1] > lst[2]:
                    return lst[1], lst[2]
                else:
                    return lst[2], lst[1]
        else:
            if lst[1] > lst[2]:
                if lst[1] > lst[3]:
                    return lst[1], lst[3]
                else:
                    return lst[3], lst[1]
            else:
                if lst[2] > lst[3]:
                    return lst[2], lst[3]
                else:
                    return lst[3], lst[2]
    if len(lst) == 5:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > lst[3]:
                    if lst[0] > lst[4]:
                        return lst[0], lst[4]
                    else:
                        return lst[4], lst[0]
                else:
                    if lst[1] > lst[3]:
                        return lst[1], lst[3]
                    else:
                        return lst[3], lst[1]
            else:
                if lst[1] > lst[2]:
                    if lst[1] > lst[3]:
                        if lst[1] > lst[4]:
                            return lst[1], lst[