
def get_sugar_water(a, b, c, d, e, f):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through possible combinations of operations
    for operation_1 in range(0, f + 1):
        for operation_2 in range(0, f + 1 - operation_1):
            for operation_3 in range(0, f + 1 - operation_1 - operation_2):
                for operation_4 in range(0, f + 1 - operation_1 - operation_2 - operation_3):
                    # Calculate the total mass of substances in the beaker
                    total_mass = operation_1 * a + operation_2 * b + operation_3 * c + operation_4 * d

                    # Check if the total mass is within the allowed range
                    if total_mass <= f:
                        # Calculate the mass of sugar water
                        sugar_water = operation_1 * a + operation_2 * b + operation_3 * c + operation_4 * d

                        # Calculate the mass of sugar dissolved
                        sugar_dissolved = operation_3 * c + operation_4 * d

                        # Check if the density of the sugar water is higher than the previous one
                        if sugar_water * 100 / (sugar_dissolved + sugar_water) > sugar_water * 100 / (sugar_dissolved + sugar_water - e):
                            # Update the solution
                            sugar_water = sugar_water
                            sugar_dissolved = sugar_dissolved

    # Return the solution
    return sugar_water, sugar_dissolved

