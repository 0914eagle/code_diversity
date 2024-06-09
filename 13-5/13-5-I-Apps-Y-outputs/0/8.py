
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / F

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made with the current combination of operations
            sugar_water = a + c

            # Check if the mass of sugar water is within the allowed range
            if sugar_water <= F:
                # Calculate the mass of sugar that can be dissolved in the current combination of operations
                sugar_dissolved = min(c, max_sugar)

                # Check if the mass of sugar water is the highest possible density
                if sugar_water * 100 / (a + sugar_dissolved) > sugar_water * 100 / (sugar_water - sugar_dissolved):
                    return [sugar_water, sugar_dissolved]

    return [0, 0]

