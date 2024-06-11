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
    elif len(lst) == 1:
        if lst[0] > 0:
            return (None, lst[0])
        elif lst[0] < 0:
            return (lst[0], None)
        else:
            return (None, None)
    else:
        lst.sort()
        if lst[0] < 0:
            return (lst[0], lst[1])
        elif lst[0] > 0:
            return (None, lst[0])
        else:
            return (None, None)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
print(largest_smallest_integers([-1, -2, -3]))
print(largest_smallest_integers([-1]))
print(largest_smallest_integers([0, 0, 0, 0, 0, 0]))
