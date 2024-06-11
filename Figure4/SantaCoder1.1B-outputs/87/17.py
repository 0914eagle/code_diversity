def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    return [x for x in lst if x[0] == x[1]]


