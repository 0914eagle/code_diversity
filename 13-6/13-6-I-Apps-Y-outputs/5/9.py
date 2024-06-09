
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_mass = a + c
            sugar_dissolved_mass = a * E / 100

            # Check if the mass of substances in the beaker is within the limit
            if sugar_water_mass + sugar_dissolved_mass <= F:
                # Check if the density of the sugar water is higher than the current best solution
                if sugar_water_mass * 100 / (sugar_dissolved_mass + sugar_water_mass) > sugar_water * 100 / (sugar_dissolved + sugar_water):
                    sugar_water = sugar_water_mass
                    sugar_dissolved = sugar_dissolved_mass

    return sugar_water, sugar_dissolved

