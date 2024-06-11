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
    else:
        largest_neg = None
        smallest_pos = None
        for i in lst:
            if i < 0:
                if largest_neg is None:
                    largest_neg = i
                elif largest_neg < i:
                    largest_neg = i
            if i > 0:
                if smallest_pos is None:
                    smallest_pos = i
                elif smallest_pos > i:
                    smallest_pos = i
        return (largest_neg, smallest_pos)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))