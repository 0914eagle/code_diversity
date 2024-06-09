
def find_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B+1):
        for c in range(C, D+1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_candidate = a + c
            sugar_dissolved_candidate = c * 100 / (a + c)

            # Check if the mass of substances in the beaker does not exceed F
            if sugar_water_candidate + sugar_dissolved_candidate <= F:
                # Check if the mass of sugar water is higher than the current highest density
                if sugar_water_candidate > sugar_water:
                    sugar_water = sugar_water_candidate
                    sugar_dissolved = sugar_dissolved_candidate

    # Return the mass of sugar water and sugar dissolved
    return sugar_water, sugar_dissolved

