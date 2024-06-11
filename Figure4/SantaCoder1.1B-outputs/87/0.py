def get_row(lst, x):
    
    # sort coordinates by rows
    lst.sort(key=lambda x: x[0])
    # sort coordinates of the row by columns
    lst.sort(key=lambda x: x[1], reverse=True)
    # find coordinates of x in the list
    lst_x = [x for x in lst if x[1] == x[0] and x[0] == x[1] + x[0]]
    # return list of tuples, [(x1, y1), (x2, y2) ...] such that
    # each tuple is a coordinate - (row, columns), starting with 0.
    return [(x[0], x[1]) for x in lst_x]


