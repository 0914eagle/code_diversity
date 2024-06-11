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
        min_value = min(lst)
        max_value = max(lst)
        new_list = [min_value, max_value]
        for i in range(2, len(lst)):
            if i % 2 == 0:
                new_list.append(min(lst))
                lst.remove(min(lst))
            else:
                new_list.append(max(lst))
                lst.remove(max(lst))
        return new_list


print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))
