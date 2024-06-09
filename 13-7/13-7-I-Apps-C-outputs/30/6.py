
def is_monotonic(grid):
    # Check if the grid is monotonic
    # Return True if the grid is monotonic, False otherwise
    pass

def count_monotonic_subgrids(grid):
    # Count the number of monotonic subgrids in the grid
    # Return the number of monotonic subgrids
    pass

def main():
    # Read the input grid
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(list(map(int, input().split())))
    
    # Count the number of monotonic subgrids in the grid
    count = count_monotonic_subgrids(grid)
    
    # Print the number of monotonic subgrids
    print(count)

if __name__ == "__main__":
    main()

