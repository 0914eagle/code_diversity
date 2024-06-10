
def get_minimum_night_count(n):
    # Initialize variables
    nights = 0
    bacteria_count = 1
    total_mass = 1

    # Loop until the total mass is equal to n
    while total_mass < n:
        # Increment the night count
        nights += 1

        # Split the bacteria
        bacteria_count *= 2

        # Increment the total mass
        total_mass += bacteria_count

    # Return the minimum night count and the number of bacteria that should split on each day
    return nights, [int(bacteria_count / 2)] * nights

def main():
    # Read the number of test cases
    t = int(input())

    # Loop through each test case
    for _ in range(t):
        # Read the target total mass
        n = int(input())

        # Get the minimum night count and the number of bacteria that should split on each day
        nights, bacteria_to_split = get_minimum_night_count(n)

        # Check if a solution exists
        if nights == -1:
            print(-1)
        else:
            # Print the minimum night count and the number of bacteria that should split on each day
            print(nights)
            print(" ".join(map(str, bacteria_to_split)))

if __name__ == '__main__':
    main()

