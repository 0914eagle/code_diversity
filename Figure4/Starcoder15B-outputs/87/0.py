def get_row(lst, x):
    
    result = []
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            if item == x:
                result.append((i, j))
    return result
