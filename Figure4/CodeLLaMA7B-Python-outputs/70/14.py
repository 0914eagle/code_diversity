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
        lst_len = len(lst)
        i = 0
        while i < lst_len:
            if i == 0:
                min_val = lst[i]
                lst.remove(min_val)
                lst.append(min_val)
                i += 1
            elif i == lst_len - 1:
                max_val = lst[i]
                lst.remove(max_val)
                lst.insert(0, max_val)
                i += 1
            else:
                min_val = lst[i]
                lst.remove(min_val)
                lst.insert(lst.index(max_val) + 1, min_val)
                i += 1
        return lst


if __name__ == '__main__':
    print(strange_sort_list([1, 2, 3, 4]))
    print(strange_sort_list([5, 5, 5, 5]))
    print(strange_sort_list([]))
