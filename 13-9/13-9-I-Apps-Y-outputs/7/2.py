
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    water_mass = 0
    sugar_mass = 0
    sugar_water_mass = 0
    sugar_water_density = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Calculate the mass of sugar water that can be made
            sugar_water_mass = a + c

            # Check if the mass of substances in the beaker is less than or equal to F
            if sugar_water_mass <= F:
                # Calculate the mass of sugar that can be dissolved in the water
                sugar_mass = min(c, E * a // 100)

                # Calculate the density of the sugar water
                sugar_water_density = sugar_mass * 100 / (a + sugar_mass)

                # Check if the density of the sugar water is higher than the current highest density
                if sugar_water_density > water_mass:
                    water_mass = a
                    sugar_mass = sugar_mass

    # Return the mass of the desired sugar water and the mass of sugar dissolved in it
    return water_mass, sugar_mass

def main():
    # Read inputs from stdin
    A, B, C, D, E, F = map(int, input().split())

    # Call the function to get the mass of the desired sugar water and the mass of sugar dissolved in it
    water_mass, sugar_mass = get_sugar_water(A, B, C, D, E, F)

    # Print the output
    print(water_mass, sugar_mass)

if __name__ == '__main__':
    main()

