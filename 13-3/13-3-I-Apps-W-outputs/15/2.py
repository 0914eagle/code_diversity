
def find_overlapping_section(map1, map2):
    # Initialize a dictionary to store the count of each cosmic object type
    cosmic_objects = {}
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            cosmic_object = map1[i][j]
            if cosmic_object not in cosmic_objects:
                cosmic_objects[cosmic_object] = 0
            cosmic_objects[cosmic_object] += 1
    
    # Find the cosmic object that appears in both maps with the highest count
    max_count = 0
    common_cosmic_object = None
    for cosmic_object, count in cosmic_objects.items():
        if count > max_count:
            max_count = count
            common_cosmic_object = cosmic_object
    
    # Find the row and column indices of the first occurrence of the common cosmic object in both maps
    row_indices = []
    col_indices = []
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] == common_cosmic_object:
                row_indices.append(i)
                col_indices.append(j)
                break
    
    # Find the maximum size of the overlapping section
    max_size = 0
    for i in range(len(row_indices)):
        for j in range(len(col_indices)):
            size = 1
            while i + size < len(row_indices) and j + size < len(col_indices) and map1[row_indices[i + size]][col_indices[j + size]] == common_cosmic_object:
                size += 1
            max_size = max(max_size, size)
    
    # Return the row and column indices of the first occurrence of the common cosmic object in both maps, with the maximum size of the overlapping section
    return row_indices[0], col_indices[0], max_size

def main():
    map1 = [list(input()) for _ in range(int(input()))]
    map2 = [list(input()) for _ in range(int(input()))]
    row_index, col_index, size = find_overlapping_section(map1, map2)
    print(f"{row_index} {col_index}")

if __name__ == '__main__':
    main()

