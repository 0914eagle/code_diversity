
def get_sugar_water_mass(A, B, C, D, E, F):
    # Initialize variables
    sugar_water_mass = 0
    sugar_dissolved_mass = 0
    
    # Iterate through all possible operations
    for a in range(A, B+1):
        for c in range(C, D+1):
            # Check if the operation is feasible
            if a + c <= F:
                # Calculate the mass of sugar water
                sugar_water_mass = a + c
                
                # Calculate the mass of sugar dissolved
                sugar_dissolved_mass = c
                
                # Check if the density is higher than the current highest density
                if sugar_water_mass * 100 / (a + sugar_dissolved_mass) > E:
                    # If the density is higher, update the variables
                    sugar_water_mass = a + c
                    sugar_dissolved_mass = c
    
    return sugar_water_mass, sugar_dissolved_mass

def main():
    A, B, C, D, E, F = map(int, input().split())
    sugar_water_mass, sugar_dissolved_mass = get_sugar_water_mass(A, B, C, D, E, F)
    print(sugar_water_mass, sugar_dissolved_mass)

if __name__ == '__main__':
    main()

