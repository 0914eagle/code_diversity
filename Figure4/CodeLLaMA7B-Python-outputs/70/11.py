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
    lst = sorted(lst)
    lst_len = len(lst)
    i = 0
    while i < lst_len:
        if i == lst_len - 1:
            return lst
        lst[i] = lst[i + 1]
        i += 2
    return lst


