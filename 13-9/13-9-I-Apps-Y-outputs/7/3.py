
def get_max_sugar_water(A, B, C, D, E, F):
    
    # Initialize the maximum mass of sugar water and sugar dissolved
    max_sugar_water = 0
    max_sugar_dissolved = 0

    # Iterate over all possible combinations of operations
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                for d in range(D+1):
                    # Calculate the mass of water and sugar in the beaker
                    water = 100*a + 100*b
                    sugar = c + d

                    # Check if the mass of substances in the beaker is within the given limit
                    if water + sugar <= F:
                        # Calculate the density of the sugar water
                        density = (100*b)/(a + b) if a + b > 0 else 0

                        # Check if the density is higher than the current maximum
                        if density > max_sugar_water:
                            max_sugar_water = density
                            max_sugar_dissolved = c

    return max_sugar_water, max_sugar_dissolved

def main():
    # Read the input
    A, B, C, D, E, F = map(int, input().split())

    # Call the function to get the maximum sugar water and sugar dissolved
    max_sugar_water, max_sugar_dissolved = get_max_sugar_water(A, B, C, D, E, F)

    # Print the output
    print(max_sugar_water, max_sugar_dissolved)

if __name__ == '__main__':
    main()

