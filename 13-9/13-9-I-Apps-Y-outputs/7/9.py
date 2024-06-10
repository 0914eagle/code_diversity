
def get_desired_sugar_water(A, B, C, D, E, F):
    # Initialize the variables
    sugar_water = 0
    sugar_dissolved = 0

    # Loop through all possible combinations of operations
    for a in range(A, B + 1):
        for c in range(C, D + 1):
            # Check if the combination is feasible
            if a + c <= F:
                # Calculate the mass of sugar water and sugar dissolved
                sugar_water += a
                sugar_dissolved += c

                # Check if the density is higher than the previous combination
                if (sugar_water * 100) // (sugar_dissolved + sugar_water) > (sugar_water * 100) // (sugar_dissolved + sugar_water - 1):
                    # Update the variables if the density is higher
                    sugar_water = a
                    sugar_dissolved = c

    return sugar_water, sugar_dissolved

def main():
    # Read the input from stdin
    A, B, C, D, E, F = map(int, input().split())

    # Call the function to get the desired sugar water
    sugar_water, sugar_dissolved = get_desired_sugar_water(A, B, C, D, E, F)

    # Print the output
    print(sugar_water, sugar_dissolved)

if __name__ == '__main__':
    main()

