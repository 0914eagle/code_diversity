def get_row(lst, x):
    
    # Sort coordinates of the row by columns in descending order
    lst.sort(key=lambda x: (-x[0], x[1]))
    # Find integers x in the list
    return [(x, lst[i][x]) for i, x in enumerate(lst[0]) if x == x]


