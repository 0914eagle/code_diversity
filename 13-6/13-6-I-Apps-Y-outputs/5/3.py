
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made with the current combination of operations
            sugar_water_temp = a + c

            # Check if the mass of sugar water is within the allowed range
            if sugar_water_temp <= F:
                # Calculate the mass of sugar dissolved in the sugar water
                sugar_dissolved_temp = (E * c) // (a + c)

                # Check if the mass of sugar dissolved is within the allowed range
                if sugar_dissolved_temp <= D:
                    # Check if the current combination of operations results in a higher density than the previous combination
                    if (sugar_water_temp * 100) // (a + c) > (sugar_water * 100) // (A + C):
                        # Update the variables with the new combination of operations
                        sugar_water = sugar_water_temp
                        sugar_dissolved = sugar_dissolved_temp

    # Return the mass of sugar water and the mass of sugar dissolved
    return sugar_water, sugar_dissolved

