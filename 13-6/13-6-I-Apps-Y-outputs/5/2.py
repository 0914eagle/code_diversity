
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
                    sugar_water_temp = i * 100 + j * 100
                    sugar_dissolved_temp = k * e + l * e

                    # Check if the sugar water is within the desired range
                    if sugar_water_temp <= f:
                        # Check if the sugar water is the highest density possible
                        if (sugar_dissolved_temp / sugar_water_temp) >= (sugar_dissolved / sugar_water):
                            sugar_water = sugar_water_temp
                            sugar_dissolved = sugar_dissolved_temp

    return [sugar_water, sugar_dissolved]

