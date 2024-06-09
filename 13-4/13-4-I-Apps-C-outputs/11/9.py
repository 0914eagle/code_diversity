
def mad(grid, a, b):
    # Initialize an empty list to store the densities
    densities = []
    
    # Iterate over the possible rectangles
    for i in range(a, b+1):
        for j in range(a, b+1):
            # Calculate the density of statisticians in the current rectangle
            density = calculate_density(grid, i, j)
            # Add the density to the list of densities
            densities.append(density)
    
    # Sort the list of densities in ascending order
    densities.sort()
    
    # Return the median of the densities
    return densities[len(densities)//2]

def calculate_density(grid, i, j):
    # Initialize a counter to store the number of statisticians
    count = 0
    
    # Iterate over the grid and count the number of statisticians in the current rectangle
    for row in grid:
        for cell in row:
            if cell >= i and cell <= j:
                count += 1
    
    # Calculate the density and return it
    return count / (i * j)

grid = [[6, 5, 2, 2], [5, 9, 7, 13]]
a = 1
b = 8
print(mad(grid, a, b))

