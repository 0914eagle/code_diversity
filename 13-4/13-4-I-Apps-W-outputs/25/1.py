
def solve(map1, map2):
    # Find the length of the common section
    n = len(set(map1).intersection(set(map2)))
    
    # Find the starting position of the common section in map1
    i = map1.index(map1[0:n])
    
    # Find the starting position of the common section in map2
    j = map2.index(map2[0:n])
    
    return i, j

