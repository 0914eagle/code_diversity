
def mad(grid, area_bounds, statisticians):
    # Initialize variables
    densities = []
    grid_height, grid_width = len(grid), len(grid[0])

    # Iterate through all possible rectangles
    for i in range(grid_height):
        for j in range(grid_width):
            for k in range(i, grid_height):
                for l in range(j, grid_width):
                    # Calculate the area of the current rectangle
                    area = (k - i + 1) * (l - j + 1)

                    # Check if the rectangle is within the allowed bounds
                    if area_bounds[0] <= area <= area_bounds[1]:
                        # Calculate the density of statisticians in the current rectangle
                        density = 0
                        for m in range(i, k + 1):
                            for n in range(j, l + 1):
                                density += grid[m][n]
                        density /= area

                        # Add the density to the list of densities
                        densities.append(densities)

    # Calculate the MAD by finding the median of the densities
    densities.sort()
    if len(densities) % 2 == 0:
        mad = (densities[len(densities) // 2 - 1] + densities[len(densities) // 2]) / 2
    else:
        mad = densities[len(densities) // 2]

    return mad

