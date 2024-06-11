def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: x[1], reverse=True)
    return [(lst[i][0], lst[i][1]) for i in range(len(lst)) if lst[i][1] == x]


