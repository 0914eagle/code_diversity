
def solve(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made with the current combination of operations
            sugar_water = a + c

            # Check if the mass of sugar water is within the allowed range
            if sugar_water <= F:
                # Calculate the mass of sugar that can be dissolved in the current combination of operations
                sugar_dissolved = (E * sugar_water) // 100

                # Check if the mass of sugar dissolved is within the allowed range
                if sugar_dissolved <= c:
                    # Return the mass of sugar water and the mass of sugar dissolved if a higher density sugar water is found
                    return [sugar_water, sugar_dissolved]

    # If no higher density sugar water is found, return -1 for both masses
    return [-1, -1]

