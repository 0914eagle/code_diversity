def get_row(lst, x):
    
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(lst)):
        if lst[i][1] == x:
            return lst[i]
    return []


