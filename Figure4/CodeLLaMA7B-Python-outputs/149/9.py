def sorted_list_sum(lst):
    
    lst.sort(key=lambda x: (len(x), x))
    return lst


