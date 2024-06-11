def sorted_list_sum(lst):
    
    lst = sorted(lst, key=lambda x: (len(x), x))
    return lst


if