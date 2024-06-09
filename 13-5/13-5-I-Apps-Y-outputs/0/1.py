
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made with the current combination of operations
            sugar_water_mass = a + c

            # Check if the mass of sugar water is within the allowed range
            if sugar_water_mass <= F:
                # Calculate the mass of sugar that can be dissolved in the current combination of operations
                sugar_dissolved_mass = a * E // 100

                # Check if the mass of sugar dissolved is within the allowed range
                if sugar_dissolved_mass <= c:
                    # Calculate the density of the sugar water
                    density = sugar_dissolved_mass * 100 / sugar_water_mass

                    # Check if the density is higher than the current highest density
                    if density > sugar_water:
                        # Update the variables with the new highest density and mass of sugar water
                        sugar_water = density
                        sugar_dissolved = sugar_dissolved_mass

    # Return the mass of sugar water and the mass of sugar dissolved
    return sugar_water, sugar_dissolved

