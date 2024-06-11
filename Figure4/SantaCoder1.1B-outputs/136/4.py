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
    if all(x < 0 for x in lst):
        return None, None
    if all(x > 0 for x in lst):
        return None, None
    if all(x == 0 for x in lst):
        return None, None
    if len(lst) == 1:
        return lst[0], lst[0]
    if len(lst) == 2:
        return max(lst), min(lst)
    if len(lst) == 3:
        return max(lst), min(lst), min(lst)
    if len(lst) == 4:
        return max(lst), min(lst), min(lst), max(lst)
    if len(lst) == 5:
        return max(lst), min(lst), min(lst), max(lst), max(lst)
    if len(lst) == 6:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst)
    if len(lst) == 7:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst)
    if len(lst) == 8:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst), max(lst)
    if len(lst) == 9:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst)
    if len(lst) == 10:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst)
    if len(lst) == 11:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max(lst)
    if len(lst) == 12:
        return max(lst), min(lst), min(lst), max(lst), max(lst), max(lst), max(lst), max(lst), max