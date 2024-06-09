
def find_common_section(map1, map2):
    # Find the length of the common section
    n = len(set(map1[0]) & set(map2[0]))
    
    # Find the row and column indices of the common section
    row_indices = [i for i, row in enumerate(map1) if set(row) == set(map2[0])]
    col_indices = [i for i, col in enumerate(zip(*map2)) if set(col) == set(map1[0])]
    
    return row_indices[0], col_indices[0]

