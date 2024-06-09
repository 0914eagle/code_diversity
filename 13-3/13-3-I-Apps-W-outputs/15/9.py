
def find_overlapping_section(map1, map2):
    # Initialize a dictionary to store the counts of each cosmic object type
    cosmic_object_counts = {}
    
    # Loop through the first map and increment the count of each cosmic object type
    for row in map1:
        for cosmic_object in row:
            if cosmic_object not in cosmic_object_counts:
                cosmic_object_counts[cosmic_object] = 1
            else:
                cosmic_object_counts[cosmic_object] += 1
    
    # Loop through the second map and find the cosmic object types that appear in both maps
    for row in map2:
        for cosmic_object in row:
            if cosmic_object in cosmic_object_counts and cosmic_object_counts[cosmic_object] > 0:
                # Decrement the count of the cosmic object type in the first map
                cosmic_object_counts[cosmic_object] -= 1
    
    # Find the cosmic object type that appears in both maps with the highest count
    max_count = 0
    max_cosmic_object = None
    for cosmic_object, count in cosmic_object_counts.items():
        if count > max_count:
            max_count = count
            max_cosmic_object = cosmic_object
    
    # Find the row and column indices of the first occurrence of the max cosmic object type in the first map
    row_index = 0
    col_index = 0
    for row in map1:
        for cosmic_object in row:
            if cosmic_object == max_cosmic_object:
                break
        else:
            row_index += 1
        break
    
    # Find the row and column indices of the first occurrence of the max cosmic object type in the second map
    for col in map2:
        for cosmic_object in col:
            if cosmic_object == max_cosmic_object:
                break
        else:
            col_index += 1
        break
    
    return row_index, col_index

def main():
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    row_index, col_index = find_overlapping_section(map1, map2)
    print(row_index, col_index)

if __name__ == '__main__':
    main()

