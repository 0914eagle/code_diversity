def get_row(lst, x):
    
    # your code here
    res = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                res.append((i, j))
    return res

