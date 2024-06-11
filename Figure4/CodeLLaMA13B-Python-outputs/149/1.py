def sorted_list_sum(lst):
    
    # lst = [i for i in lst if len(i) % 2 == 0]
    # lst.sort(key=len)
    # return lst
    return sorted(filter(lambda x: len(x) % 2 == 0, lst), key=len)
