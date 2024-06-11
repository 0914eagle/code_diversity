def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return lst
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return [lst[0], lst[1]]
    if len(lst) == 3:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                return [lst[1], lst[0], lst[2]]
            else:
                return [lst[1], lst[0]]
        else:
            if lst[1] > lst[2]:
                return [lst[0], lst[1], lst[2]]
            else:
                return [lst[0], lst[1]]
    if len(lst) == 4:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > lst[3]:
                    return [lst[1], lst[0], lst[3]]
                else:
                    return [lst[1], lst[0], lst[2]]
            else:
                if lst[1] > lst[2]:
                    return [lst[0], lst[1], lst[2]]
                else:
                    return [lst[0], lst[1]]
        else:
            if lst[1] > lst[2]:
                if lst[1] > lst[3]:
                    return [lst[0], lst[1], lst[3]]
                else:
                    return [lst[0], lst[1], lst[2]]
            else:
                if lst[2] > lst[3]:
                    return [lst[0], lst[1], lst[2], lst[3]]
                else:
                    return [lst[0], lst[1], lst[2]]
    if len(lst) == 5:
        if lst[0] > lst[1]:
            if lst[0] > lst[2]:
                if lst[0] > lst[3]:
                    if lst[0] > lst[4]:
                        return [lst[1], lst[0], lst[4]]
                    else:
                        return [lst[1], lst[0], lst[3]]
                else:
                    return [lst[1], lst[0], lst[2]]
            else:
                if lst[1