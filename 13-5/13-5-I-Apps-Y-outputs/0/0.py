
def solve(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_temp = a + c
            sugar_dissolved_temp = c

            # Check if the mass of substances in the beaker is within the limit
            if sugar_water_temp <= F:
                # Calculate the density of the sugar water
                density = sugar_dissolved_temp * 100 / sugar_water_temp

                # Check if the density is higher than the current best density
                if density > sugar_water:
                    # Update the best density and the corresponding sugar water and sugar dissolved
                    sugar_water = density
                    sugar_water_final = sugar_water_temp
                    sugar_dissolved_final = sugar_dissolved_temp

    # Return the mass of the desired sugar water and the mass of sugar dissolved in it
    return sugar_water_final, sugar_dissolved_final

