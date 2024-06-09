
def align_maps(map1, map2):
    # Find the length of the common section
    n = len(set(map1[0]) & set(map2[0]))
    
    # Find the row and column indices of the common section
    row_indices = [i for i, row in enumerate(map1) if row[:n] == map2[0][:n]]
    col_indices = [j for j, col in enumerate(zip(*map2)) if col[:n] == zip(*map1)[0][:n]]
    
    return row_indices[0], col_indices[0]

