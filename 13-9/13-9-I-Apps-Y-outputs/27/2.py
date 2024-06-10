
def read_input():
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    return n, m, k, grid

def find_paths(grid, k):
    # Initialize the number of paths to 0
    num_paths = 0
    
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is the bottom-right cell, check if the xor sum is equal to k
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                if grid[i][j] ^ k == 0:
                    num_paths += 1
            # If the current cell is not the bottom-right cell, recursively call the function for the next cell
            else:
                if j < len(grid[0]) - 1:
                    num_paths += find_paths(grid, k ^ grid[i][j])
                if i < len(grid) - 1:
                    num_paths += find_paths(grid, k ^ grid[i][j])
    
    return num_paths

def main():
    n, m, k, grid = read_input()
    print(find_paths(grid, k))

if __name__ == '__main__':
    main()

