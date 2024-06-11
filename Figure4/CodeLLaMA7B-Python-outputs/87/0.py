def get_row(lst, x):
    
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result


