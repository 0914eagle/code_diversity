
def solve(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / A

    # Loop through all possible combinations of operations
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(min(C, max_sugar) + 1):
                for l in range(min(D, max_sugar - k) + 1):
                    # Calculate the total mass of sugar and water in the beaker
                    total_mass = i * A + j * B + k + l

                    # Check if the total mass is within the allowed range
                    if total_mass <= F:
                        # Calculate the density of the sugar water
                        density = (k * 100) / (i * A + j * B + k + l)

                        # Check if the density is higher than the current best density
                        if density > sugar_water:
                            sugar_water = density
                            sugar_dissolved = k

    # Return the results
    return sugar_water, sugar_dissolved

