
def find_overlapping_section(map1, map2):
    # Initialize a dictionary to store the count of each cosmic object type
    cosmic_object_count = {}
    
    # Loop through the first map and increment the count of each cosmic object type
    for row in map1:
        for char in row:
            if char not in cosmic_object_count:
                cosmic_object_count[char] = 1
            else:
                cosmic_object_count[char] += 1
    
    # Loop through the second map and find the cosmic object types that appear in both maps
    for row in map2:
        for char in row:
            if char in cosmic_object_count and cosmic_object_count[char] > 0:
                # Decrement the count of the cosmic object type in the first map
                cosmic_object_count[char] -= 1
    
    # Find the cosmic object type with the smallest count that is non-zero
    smallest_count = float('inf')
    smallest_cosmic_object = None
    for char, count in cosmic_object_count.items():
        if count > 0 and count < smallest_count:
            smallest_count = count
            smallest_cosmic_object = char
    
    # Find the row and column indices of the smallest cosmic object type in the first map
    row_index = 0
    for row in map1:
        if smallest_cosmic_object in row:
            break
        row_index += 1
    col_index = row.index(smallest_cosmic_object)
    
    return row_index, col_index

def main():
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    row_index, col_index = find_overlapping_section(map1, map2)
    print(row_index, col_index)

if __name__ == '__main__':
    main()

