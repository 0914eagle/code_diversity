
def solve(a, b, c, d, e, f):
    # Initialize the variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                for l in range(d + 1):
                    # Calculate the mass of sugar water and sugar dissolved
                    mass_sugar_water = i * 100 + j * 100
                    mass_sugar_dissolved = k * e + l * e

                    # Check if the mass of sugar water is within the limits
                    if mass_sugar_water <= f:
                        # Calculate the density of the sugar water
                        density = mass_sugar_dissolved * 100 / mass_sugar_water

                        # Check if the density is the highest so far
                        if density > sugar_water:
                            sugar_water = mass_sugar_water
                            sugar_dissolved = mass_sugar_dissolved

    # Return the results
    return sugar_water, sugar_dissolved

