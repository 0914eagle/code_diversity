
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 // A

    # Loop through all possible combinations of operations
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                for l in range(D + 1):
                    # Calculate the total mass of water and sugar in the beaker
                    total_water = i * A + j * B
                    total_sugar = k * C + l * D

                    # Check if the total mass of substances in the beaker is within the given limit
                    if total_water + total_sugar <= F:
                        # Calculate the density of the sugar water
                        density = total_sugar * 100 / (total_water + total_sugar)

                        # Check if the density is higher than the current best density
                        if density > sugar_water:
                            sugar_water = density
                            sugar_dissolved = total_sugar

    # Return the mass of the desired sugar water and the mass of sugar dissolved in it
    return sugar_water, sugar_dissolved

