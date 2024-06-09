
def get_sugar_water(A, B, C, D, E, F):
    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / A

    # Initialize the variables to track the best solution
    best_sugar_water = 0
    best_sugar = 0

    # Iterate over the possible ranges of sugar and water
    for sugar in range(C, D + 1):
        for water in range(A, B + 1):
            # Calculate the total amount of substances in the beaker
            total_substances = sugar + water

            # Check if the total amount of substances is within the limit
            if total_substances <= F:
                # Calculate the density of the sugar water
                density = water * 100 / (sugar + water)

                # Check if the density is higher than the current best density
                if density > best_sugar_water:
                    # Update the best density and sugar amount
                    best_sugar_water = density
                    best_sugar = sugar

    # Return the best solution
    return best_sugar_water, best_sugar

