def sorted_list_sum(lst):
    
    # your code here
    # lst = [x for x in lst if len(x) % 2 == 0]
    # lst.sort(key=len)
    # return lst
    return sorted([x for x in lst if len(x) % 2 == 0], key=len)


if __