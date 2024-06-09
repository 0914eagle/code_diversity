
def align_maps(map1, map2):
    # Find the length of the common section
    n = len(set(map1).intersection(set(map2)))
    
    # Find the starting indices of the common section in both maps
    i = map1.index(map1[:n])
    j = map2.index(map2[:n])
    
    return i, j

