
def get_non_empty_sets(table):
    # Initialize a set to store the non-empty sets
    non_empty_sets = set()
    
    # Loop through each row of the table
    for row in table:
        # Loop through each cell in the row
        for i in range(len(row)):
            # If the cell is white, skip to the next cell
            if row[i] == 0:
                continue
            # If the cell is black, add it to the non-empty set
            non_empty_sets.add((i, row[i]))
    
    # Return the number of non-empty sets
    return len(non_empty_sets)

def main():
    # Read the number of rows and columns from stdin
    n, m = map(int, input().split())
    
    # Initialize the table as a list of lists
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    
    # Get the number of non-empty sets
    non_empty_sets = get_non_empty_sets(table)
    
    # Print the number of non-empty sets
    print(non_empty_sets)

if __name__ == '__main__':
    main()

