
def get_non_empty_sets(table):
    # Initialize a set to store the non-empty sets
    non_empty_sets = set()
    
    # Iterate over the rows of the table
    for i in range(len(table)):
        # Iterate over the columns of the table
        for j in range(len(table[i])):
            # If the current cell is colored black, add it to the non-empty sets
            if table[i][j] == 1:
                non_empty_sets.add((i, j))
    
    # Return the number of non-empty sets
    return len(non_empty_sets)

def main():
    # Read the number of rows and columns from stdin
    n, m = map(int, input().split())
    
    # Initialize the table as a list of lists of zeros
    table = [[0] * m for _ in range(n)]
    
    # Read the table from stdin
    for i in range(n):
        table[i] = list(map(int, input().split()))
    
    # Get the number of non-empty sets
    non_empty_sets = get_non_empty_sets(table)
    
    # Print the number of non-empty sets
    print(non_empty_sets)

if __name__ == '__main__':
    main()

