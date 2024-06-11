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
        return []
    min_val = min(lst)
    max_val = max(lst)
    result = []
    while lst:
        if lst[0] == min_val:
            result.append(min_val)
            lst.remove(min_val)
            if lst:
                max_val = max(lst)
        elif lst[0] == max_val:
            result.append(max_val)
            lst.remove(max_val)
            if lst:
                min_val = min(lst)
    return result


