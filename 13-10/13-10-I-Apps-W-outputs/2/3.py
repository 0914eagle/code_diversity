
def count_sets(grid):
    # Initialize a dictionary to store the sets
    sets = {}
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # If the current cell is white, skip it
            if grid[i][j] == 0:
                continue
            # If the current cell is black, find the set it belongs to
            set_id = find_set(sets, i, j)
            # If the set does not exist, create a new set with the current cell as its representative
            if set_id not in sets:
                sets[set_id] = set()
            # Add the current cell to the set
            sets[set_id].add((i, j))
    
    # Return the number of sets
    return len(sets)

def find_set(sets, i, j):
    # Find the representative of the set that the cell (i, j) belongs to
    representative = (i, j)
    while representative in sets:
        representative = sets[representative]
    # Find the set ID of the representative
    set_id = representative
    # Update the set ID of the cell (i, j)
    sets[(i, j)] = set_id
    return set_id

def main():
    # Read the input grid
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    # Count the number of sets
    count = count_sets(grid)
    
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

