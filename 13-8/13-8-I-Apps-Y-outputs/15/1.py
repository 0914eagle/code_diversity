
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made
            sugar_water_temp = a + c

            # Check if the mass of sugar water is within the limits
            if sugar_water_temp <= F:
                # Calculate the mass of sugar dissolved in the sugar water
                sugar_dissolved_temp = (c * E) // 100

                # Check if the mass of sugar dissolved is within the limits
                if sugar_dissolved_temp <= sugar_water_temp:
                    # Update the mass of sugar water and sugar dissolved if necessary
                    if sugar_water_temp > sugar_water:
                        sugar_water = sugar_water_temp
                        sugar_dissolved = sugar_dissolved_temp

    # Return the mass of sugar water and sugar dissolved
    return sugar_water, sugar_dissolved

