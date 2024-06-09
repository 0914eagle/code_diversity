
def mad(grid, a, b):
    # Initialize empty list to store densities
    densities = []

    # Loop through all possible rectangles
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            # Calculate density of statisticians in current rectangle
            density = calculate_density(grid, i, j)
            densities.append(density)

    # Return median of densities
    return median(densities)

def calculate_density(grid, i, j):
    # Initialize sum of statisticians in current rectangle
    sum = 0

    # Loop through all squares in current rectangle
    for x in range(i):
        for y in range(j):
            # Add number of statisticians in current square to sum
            sum += grid[x][y]

    # Return density of statisticians in current rectangle
    return sum / (i * j)

def median(my_list):
    # Sort list
    my_list.sort()

    # Check if list has odd or even number of elements
    if len(my_list) % 2 == 0:
        # If even, return mean of two middle elements
        mid = len(my_list) // 2
        return (my_list[mid] + my_list[mid - 1]) / 2
    else:
        # If odd, return middle element
        mid = len(my_list) // 2
        return my_list[mid]

