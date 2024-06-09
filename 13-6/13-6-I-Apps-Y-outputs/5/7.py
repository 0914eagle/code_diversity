
def solve(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B+1):
        for c in range(C, D+1):
            # Calculate the mass of sugar water and sugar dissolved
            sugar_water_temp = a + c
            sugar_dissolved_temp = (100*c)/(a+c)

            # Check if the sugar water is within the maximum capacity of the beaker
            if sugar_water_temp <= F:
                # Check if the sugar water has higher density than the current solution
                if sugar_dissolved_temp > sugar_dissolved:
                    sugar_water = sugar_water_temp
                    sugar_dissolved = sugar_dissolved_temp

    # Return the results
    return sugar_water, sugar_dissolved

