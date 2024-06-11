def sorted_list_sum(lst):
    
    lst = sorted(lst, key=len)
    lst = [x for x in lst if len(x) % 2 == 0]
    return sorted(lst)


if