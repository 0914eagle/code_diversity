def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    for i in range(len(lst)):
        if lst[i][0] == x:
            return lst[i]
    return []


