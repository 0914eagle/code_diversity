
def get_sugar_water(a, b, c, d, e, f):
    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = e * f // 100

    # Initialize the mass of sugar water and sugar dissolved
    mass_sugar_water = 0
    mass_sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                for l in range(d + 1):
                    # Calculate the total mass of water and sugar in the beaker
                    total_water = i * 100 + j * 100
                    total_sugar = k * c + l * d

                    # Check if the total mass of sugar and water does not exceed the maximum capacity of the beaker
                    if total_water + total_sugar <= f:
                        # Calculate the mass of sugar water and sugar dissolved
                        mass_sugar_water_temp = total_water + total_sugar
                        mass_sugar_dissolved_temp = min(total_sugar, max_sugar)

                        # Check if the mass of sugar water and sugar dissolved is higher than the current solution
                        if mass_sugar_water_temp > mass_sugar_water:
                            mass_sugar_water = mass_sugar_water_temp
                            mass_sugar_dissolved = mass_sugar_dissolved_temp

    return mass_sugar_water, mass_sugar_dissolved

