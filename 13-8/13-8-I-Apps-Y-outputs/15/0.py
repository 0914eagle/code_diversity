
def solve(A, B, C, D, E, F):
    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / A

    # Initialize the variables to keep track of the best solution
    best_density = 0
    best_sugar = 0
    best_water = 0

    # Iterate over all possible combinations of operations
    for operation1 in range(A + 1):
        for operation2 in range(B + 1):
            for operation3 in range(C + 1):
                for operation4 in range(D + 1):
                    # Calculate the total amount of water and sugar used
                    total_water = operation1 * A + operation2 * B
                    total_sugar = operation3 * C + operation4 * D

                    # Check if the total amount of water and sugar used does not exceed the maximum amount allowed
                    if total_water + total_sugar <= F:
                        # Calculate the density of the sugar water
                        density = total_sugar * 100 / (total_water + total_sugar)

                        # Check if the density is higher than the current best density
                        if density > best_density:
                            # Update the best density, sugar, and water
                            best_density = density
                            best_sugar = total_sugar
                            best_water = total_water

    # Return the best solution
    return [best_water, best_sugar]

