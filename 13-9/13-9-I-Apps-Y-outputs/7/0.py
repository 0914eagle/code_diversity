
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    max_density = 0
    sugar_water_mass = 0
    sugar_mass = 0
    
    # Iterate over all possible combinations of operations
    for a in range(A, B+1):
        for c in range(C, D+1):
            # Calculate the density of the sugar water
            density = (100*c)/(a+c)
            # Calculate the mass of the sugar water
            sugar_water_mass = a + c
            # Calculate the mass of the sugar
            sugar_mass = c
            # Check if the density is higher than the current maximum density
            if density > max_density:
                max_density = density
                sugar_water_mass = a + c
                sugar_mass = c
    
    # Check if the mass of substances in the beaker exceeds the maximum limit
    if sugar_water_mass + sugar_mass <= F:
        return [sugar_water_mass, sugar_mass]
    else:
        return [-1, -1]

def main():
    # Read inputs from stdin
    A, B, C, D, E, F = map(int, input().split())
    # Get the sugar water and sugar mass
    sugar_water_mass, sugar_mass = get_sugar_water(A, B, C, D, E, F)
    # Print the outputs
    print(sugar_water_mass, sugar_mass)

if __name__ == '__main__':
    main()

