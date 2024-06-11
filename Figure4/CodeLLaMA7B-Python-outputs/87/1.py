def get_row(lst, x):
    
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                result.append((i, len(row) - j - 1))
    return sorted(result, key=lambda x: (x[0], -x[1]))


