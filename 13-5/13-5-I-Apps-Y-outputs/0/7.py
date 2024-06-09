
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_temp = a + c
            sugar_dissolved_temp = a * E // 100

            # Check if the mass of sugar water and sugar dissolved is within the constraints
            if sugar_water_temp <= F and sugar_dissolved_temp <= c:
                # Check if the density of the sugar water is higher than the current best solution
                if sugar_water_temp * 100 / (sugar_dissolved_temp + sugar_water_temp) > sugar_water * 100 / (sugar_dissolved + sugar_water):
                    sugar_water = sugar_water_temp
                    sugar_dissolved = sugar_dissolved_temp

    # Return the mass of sugar water and sugar dissolved
    return sugar_water, sugar_dissolved

