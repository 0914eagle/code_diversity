
def count_non_empty_sets(n, m, table):
    # Initialize a set to store the non-empty sets
    non_empty_sets = set()
    
    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(m):
            # If the current cell is black
            if table[i][j] == 1:
                # Find the non-empty sets that contain the current cell
                non_empty_sets |= find_non_empty_sets(i, j, table)
    
    # Return the number of non-empty sets
    return len(non_empty_sets)

def find_non_empty_sets(i, j, table):
    # Initialize a set to store the non-empty sets that contain the current cell
    non_empty_sets = set()
    
    # Add the current cell to the set
    non_empty_sets.add((i, j))
    
    # Iterate over the rows below the current row
    for k in range(i+1, len(table)):
        # If the current cell in the next row is black
        if table[k][j] == 1:
            # Add the cell to the set
            non_empty_sets.add((k, j))
    
    # Iterate over the columns to the right of the current column
    for k in range(j+1, len(table[0])):
        # If the current cell in the next column is black
        if table[i][k] == 1:
            # Add the cell to the set
            non_empty_sets.add((i, k))
    
    # Return the set of non-empty sets that contain the current cell
    return non_empty_sets

if __name__ == '__main__':
    # Read the input
    n, m = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    
    # Call the count_non_empty_sets function
    result = count_non_empty_sets(n, m, table)
    
    # Print the result
    print(result)

