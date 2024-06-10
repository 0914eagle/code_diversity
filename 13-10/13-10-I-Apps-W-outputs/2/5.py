
def get_input():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    return n, m, table

def solve(n, m, table):
    # Initialize a dictionary to store the number of non-empty sets
    num_sets = 0
    
    # Iterate through each row of the table
    for i in range(n):
        # Initialize a set to store the colors in the current row
        row_colors = set()
        # Iterate through each cell in the current row
        for j in range(m):
            # If the current cell is colored black, add it to the set of row colors
            if table[i][j] == 1:
                row_colors.add(j)
        # If the set of row colors is not empty, add it to the total number of non-empty sets
        if row_colors:
            num_sets += 1
    
    # Return the total number of non-empty sets
    return num_sets

def main():
    n, m, table = get_input()
    print(solve(n, m, table))

if __name__ == '__main__':
    main()

