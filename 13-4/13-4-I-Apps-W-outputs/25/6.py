
def find_overlapping_section(map1, map2):
    # Find the length of the shortest map
    shortest_map_length = min(len(map1), len(map2))
    
    # Iterate through the shortest map and find the first row that is the same in both maps
    for i in range(shortest_map_length):
        if map1[i] == map2[i]:
            # Find the column in the second map that matches the first row in the first map
            for j in range(shortest_map_length):
                if map1[i][j] == map2[0][j]:
                    return i + 1, j + 1
    
    # If no matching row is found, return -1, -1
    return -1, -1

