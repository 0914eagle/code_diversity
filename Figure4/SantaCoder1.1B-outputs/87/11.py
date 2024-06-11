def get_row(lst, x):
    
    # Your code here
    lst = sorted(lst, key=lambda x: x[0])
    for i in range(len(lst)):
        if lst[i][0] == x:
            return lst[i][1:]
    return []

