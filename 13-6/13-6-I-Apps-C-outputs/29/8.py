
def mad(grid, a, b):
    # Initialize an empty list to store the densities
    densities = []

    # Iterate over each possible rectangle
    for i in range(a, b + 1):
        # Calculate the density of statisticians in the current rectangle
        density = calculate_density(grid, i)

        # Add the density to the list of densities
        densities.append(density)

    # Return the median of the densities
    return median(densities)

def calculate_density(grid, area):
    # Initialize a counter for the number of statisticians
    count = 0

    # Iterate over each square in the grid
    for row in grid:
        for cell in row:
            # Check if the current square is within the rectangle
            if cell >= area:
                # Increment the counter
                count += 1

    # Return the density as the number of statisticians per square
    return count / (len(grid) * len(grid[0]))

def median(my_list):
    # Sort the list
    my_list.sort()

    # Check if the list has an odd or even number of elements
    if len(my_list) % 2 == 0:
        # If the list has an even number of elements, return the mean of the two middle elements
        mid = len(my_list) // 2
        return (my_list[mid - 1] + my_list[mid]) / 2
    else:
        # If the list has an odd number of elements, return the middle element
        mid = len(my_list) // 2
        return my_list[mid]

