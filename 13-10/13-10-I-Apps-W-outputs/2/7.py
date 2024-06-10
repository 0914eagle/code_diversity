
def get_non_empty_sets(table):
    # Initialize a set to store the non-empty sets
    non_empty_sets = set()
    
    # Loop through each row of the table
    for row in table:
        # Loop through each cell in the row
        for i in range(len(row)):
            # Check if the cell is black
            if row[i] == 1:
                # If the cell is black, add it to the set of non-empty sets
                non_empty_sets.add(frozenset([(i, j) for j, cell in enumerate(row) if cell == 1]))
    
    # Return the number of non-empty sets
    return len(non_empty_sets)

def main():
    # Read the number of rows and columns from stdin
    n, m = map(int, input().split())
    
    # Initialize the table with the given dimensions
    table = [[0] * m for _ in range(n)]
    
    # Read the table from stdin
    for i in range(n):
        row = list(map(int, input().split()))
        for j, cell in enumerate(row):
            table[i][j] = cell
    
    # Get the number of non-empty sets
    non_empty_sets = get_non_empty_sets(table)
    
    # Print the number of non-empty sets
    print(non_empty_sets)

if __name__ == '__main__':
    main()

