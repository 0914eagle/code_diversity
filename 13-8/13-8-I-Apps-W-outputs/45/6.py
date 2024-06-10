
def get_total_mass(bacteria_mass, n):
    # Initialize variables
    total_mass = 0
    nights = 0
    bacteria = [bacteria_mass]

    # Loop through nights
    while total_mass < n:
        # Increment nights
        nights += 1

        # Split bacteria
        new_bacteria = []
        for b in bacteria:
            if b >= 2:
                new_bacteria.append(b / 2)
                new_bacteria.append(b / 2)
            else:
                new_bacteria.append(b)
        bacteria = new_bacteria

        # Increment bacteria mass
        for i in range(len(bacteria)):
            bacteria[i] += 1

        # Calculate total mass
        total_mass = sum(bacteria)

    # Return results
    return nights, bacteria

def main():
    # Test cases
    test_cases = int(input())
    for i in range(test_cases):
        # Read input
        n = int(input())

        # Get total mass
        nights, bacteria = get_total_mass(1, n)

        # Check if total mass is possible
        if nights == -1:
            print(-1)
        else:
            # Print output
            print(nights)
            for b in bacteria:
                print(int(b))

if __name__ == '__main__':
    main()

