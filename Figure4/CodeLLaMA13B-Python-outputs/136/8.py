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
    else:
        negative_lst = [x for x in lst if x < 0]
        positive_lst = [x for x in lst if x > 0]
        if negative_lst:
            negative_lst.sort()
            negative_lst.reverse()
            negative_integer = negative_lst[0]
        else:
            negative_integer = None
        if positive_lst:
            positive_lst.sort()
            positive_integer = positive_lst[0]
        else:
            positive_integer = None
        return negative_integer, positive_integer


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
