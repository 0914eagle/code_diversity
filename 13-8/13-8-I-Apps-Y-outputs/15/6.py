
def get_sugar_water(A, B, C, D, E, F):
    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / F
    
    # Initialize the variables to track the best solution
    best_sugar_water = 0
    best_sugar = 0
    
    # Iterate over all possible combinations of operations
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                for d in range(D+1):
                    # Calculate the total amount of water and sugar in the beaker
                    total_water = a * 100 + b * 100
                    total_sugar = c + d
                    
                    # Check if the total amount of sugar is within the limit
                    if total_sugar <= max_sugar:
                        # Calculate the density of the sugar water
                        density = total_sugar * 100 / total_water
                        
                        # Check if the density is higher than the current best solution
                        if density > best_sugar_water:
                            best_sugar_water = density
                            best_sugar = total_sugar
    
    # Return the best solution
    return (best_sugar_water, best_sugar)

