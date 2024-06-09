
def solve(A, B, C, D, E, F):
    # Initialize the variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water = a + c
            sugar_dissolved = c

            # Check if the sugar water is within the given limits
            if sugar_water <= F:
                # Calculate the density of the sugar water
                density = sugar_dissolved * 100 / sugar_water

                # Check if the density is higher than the current highest density
                if density > highest_density:
                    # Update the highest density and the corresponding mass of sugar water and sugar dissolved
                    highest_density = density
                    sugar_water_max = sugar_water
                    sugar_dissolved_max = sugar_dissolved

    # Return the mass of sugar water and sugar dissolved with the highest density
    return sugar_water_max, sugar_dissolved_max

