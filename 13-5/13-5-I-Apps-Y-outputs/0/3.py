
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_temp = a + c
            sugar_dissolved_temp = c * 100 / (a + c)

            # Check if the sugar water is within the desired density range
            if sugar_dissolved_temp >= E:
                # Check if the mass of substances in the beaker is within the desired range
                if sugar_water_temp <= F:
                    # Update the maximum mass of sugar water and sugar dissolved if necessary
                    if sugar_water_temp > sugar_water:
                        sugar_water = sugar_water_temp
                        sugar_dissolved = sugar_dissolved_temp

    # Return the maximum mass of sugar water and sugar dissolved
    return sugar_water, sugar_dissolved

