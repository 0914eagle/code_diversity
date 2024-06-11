def get_row(lst, x):
    
    # Sort coordinates by rows in ascending order
    lst.sort(key=lambda x: x[0])
    # Sort coordinates of the row by columns in descending order
    lst.sort(key=lambda x: x[1], reverse=True)
    # Find coordinates of x in the list
    return [(lst[i][0], lst[i][1]) for i in range(len(lst)) if lst[i][0] == x]

