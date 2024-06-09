
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
    
    # Find the cosmic object type that appears in both maps with the minimum count
    min_count = float('inf')
    min_cosmic_object = None
    for char, count in cosmic_object_count.items():
        if count < min_count:
            min_count = count
            min_cosmic_object = char
    
    # Find the row and column indices of the first occurrence of the minimum cosmic object type in the first map
    row_index = 0
    col_index = 0
    for row in map1:
        for char in row:
            if char == min_cosmic_object:
                break
        else:
            row_index += 1
        break
    
    for char in map1[row_index]:
        if char == min_cosmic_object:
            break
        col_index += 1
    
    return row_index, col_index

def main():
    map1 = []
    map2 = []
    
    # Read the input from stdin
    for _ in range(int(input())):
        map1.append(input())
        map2.append(input())
    
    # Find the overlapping section in the maps
    row_index, col_index = find_overlapping_section(map1, map2)
    
    # Print the row and column indices of the overlapping section
    print(row_index, col_index)

if __name__ == '__main__':
    main()

