def sorted_list_sum(lst):
    
    lst = sorted(lst, key=len)
    lst = [i for i in lst if len(i) % 2 == 0]
    return sorted(lst)


if