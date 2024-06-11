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
    lst.sort()
    min_val = lst[0]
    max_val = lst[-1]
    lst.remove(min_val)
    lst.remove(max_val)
    lst.insert(0, min_val)
    lst.append(max_val)
    return lst


if __name__ == '__main__':
    print(strange_sort_list([1, 2,