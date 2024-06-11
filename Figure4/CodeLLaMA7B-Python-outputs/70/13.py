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
    if len(lst) == 0:
        return []
    else:
        lst.sort()
        min_val = min(lst)
        max_val = max(lst)
        result = []
        while len(lst) > 0:
            if lst[0] == min_val:
                result.append(min_val)
                lst.remove(min_val)
            elif lst[0] == max_val:
                result.append(max_val)
                lst.remove(max_val)
            else:
                result.append(lst[0])
                lst.remove(lst[0])
        return result


