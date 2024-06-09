
def get_sugar_water(A, B, C, D, E, F):
    # Initialize the variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_mass = a + c
            sugar_dissolved_mass = c * 100 / (a + c)

            # Check if the sugar water is within the desired range
            if sugar_water_mass <= F:
                # Calculate the density of the sugar water
                density = sugar_dissolved_mass / sugar_water_mass

                # Check if the density is higher than the current density
                if density > sugar_water:
                    sugar_water = density
                    sugar_dissolved = sugar_dissolved_mass

    # Return the results
    return sugar_water, sugar_dissolved

