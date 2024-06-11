def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    return [(lst[i][1], i) for i in range(len(lst)) if lst[i][0] == x]

