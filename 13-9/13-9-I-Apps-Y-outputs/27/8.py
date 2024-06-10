
def get_number_of_paths(grid, k):
    # Initialize the number of paths to 0
    number_of_paths = 0
    
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is the bottom-right cell, check if the xor sum is equal to k
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                if grid[i][j] ^ k == 0:
                    number_of_paths += 1
            # If the current cell is not the bottom-right cell, recursively call the function with the next cell
            else:
                if j < len(grid[0]) - 1:
                    number_of_paths += get_number_of_paths(grid, k ^ grid[i][j])
                if i < len(grid) - 1:
                    number_of_paths += get_number_of_paths(grid, k ^ grid[i][j])
    
    # Return the number of paths
    return number_of_paths

def main():
    # Read the input grid and k
    n, m, k = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # Call the get_number_of_paths function and print the result
    print(get_number_of_paths(grid, k))

if __name__ == '__main__':
    main()

