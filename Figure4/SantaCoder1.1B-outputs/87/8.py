def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    return [(i, lst[i].index(x)) for i in range(len(lst)) if x in lst[i]]


