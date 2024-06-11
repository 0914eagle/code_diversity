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
    elif len(lst) == 1:
        return lst
    else:
        lst.sort()
        lst_min = min(lst)
        lst_max = max(lst)
        lst_new = []
        while len(lst) > 0:
            if lst_min in lst:
                lst_new.append(lst_min)
                lst.remove(lst_min)
            if lst_max in lst:
                lst_new.append(lst_max)
                lst.remove(lst_max)
            if lst_min not in lst and lst_max not in lst:
                break
        return lst_new


