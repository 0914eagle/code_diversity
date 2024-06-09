
def solve(a, b, c, d, e, f):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                for l in range(d + 1):
                    # Calculate the mass of sugar water and sugar dissolved
                    sugar_water_temp = i * 100 + j * 100 + k * e + l * e
                    sugar_dissolved_temp = k + l

                    # Check if the mass of sugar water and sugar dissolved is within the constraints
                    if sugar_water_temp <= f and sugar_dissolved_temp <= e:
                        # Check if the density of the sugar water is higher than the current best solution
                        if sugar_water_temp * 100 / (sugar_dissolved_temp + sugar_water_temp) > sugar_water * 100 / (sugar_dissolved + sugar_water):
                            # Update the best solution
                            sugar_water = sugar_water_temp
                            sugar_dissolved = sugar_dissolved_temp

    # Return the best solution
    return sugar_water, sugar_dissolved

