
def get_sugar_water(A, B, C, D, E, F):
    # Initialize the maximum density and the corresponding sugar and water masses
    max_density = 0
    sugar_mass = 0
    water_mass = 0
    
    # Iterate over all possible combinations of sugar and water masses
    for water_mass in range(A, F + 1):
        for sugar_mass in range(C, D + 1):
            # Calculate the density of the current combination
            density = (sugar_mass * 100) / (water_mass + sugar_mass)
            # Check if the current combination has the maximum density
            if density > max_density:
                max_density = density
                water_mass = water_mass
                sugar_mass = sugar_mass
    
    # Return the sugar and water masses with the maximum density
    return sugar_mass, water_mass

