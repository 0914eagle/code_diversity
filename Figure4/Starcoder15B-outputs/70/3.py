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
    if len(lst) == 1:
        return lst
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    if min_index < max_index:
        return [lst[min_index]] + strange_sort_list(lst[:min_index] + lst[min_index+1:max_index] + lst[max_index+1:]) + [lst[max_index]]
    else:
        return [lst[max_index]] + strange_sort_list(lst[:max_index] + lst[max_index+1:min_index] + lst[min_index+1:]) + [lst[min_index]]

