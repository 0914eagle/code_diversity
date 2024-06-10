
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
    
    # Loop through the second map and find the row and column indices where the cosmic object types match
    for row_index, row in enumerate(map2):
        for col_index, cosmic_object in enumerate(row):
            if cosmic_object in cosmic_object_counts and cosmic_object_counts[cosmic_object] > 0:
                return row_index + 1, col_index + 1
    
    # If no matching cosmic object types are found, return None
    return None

def main():
    # Read the input maps from stdin
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    
    # Find the overlapping section in the maps
    row_index, col_index = find_overlapping_section(map1, map2)
    
    # Print the row and column indices of the overlapping section
    print(row_index, col_index)
    
if __name__ == '__main__':
    main()

