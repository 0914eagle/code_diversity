
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made with the current combination of operations
            mass_sugar_water = a + c

            # Check if the mass of sugar water is within the maximum capacity of the beaker
            if mass_sugar_water <= F:
                # Calculate the mass of sugar dissolved in the sugar water
                mass_sugar_dissolved = (c * 100) // (a + c)

                # Check if the mass of sugar dissolved is within the maximum amount that can dissolve in the water
                if mass_sugar_dissolved <= E:
                    # Check if the current combination of operations results in a higher density than the previous ones
                    if mass_sugar_dissolved > sugar_dissolved:
                        sugar_water = mass_sugar_water
                        sugar_dissolved = mass_sugar_dissolved

    return sugar_water, sugar_dissolved

