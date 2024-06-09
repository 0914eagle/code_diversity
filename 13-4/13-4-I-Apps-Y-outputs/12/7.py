
def get_volume(L):
    
    # Initialize the maximum volume
    max_volume = 0

    # Iterate over all possible combinations of dimensions
    for a in range(1, L + 1):
        for b in range(1, L + 1):
            for c in range(1, L + 1):
                # Calculate the volume of the current cuboid
                volume = a * b * c

                # Check if the volume is greater than the maximum volume
                if volume > max_volume:
                    max_volume = volume

    return max_volume

def main():
    # Read the input from stdin
    L = int(input())

    # Calculate the maximum volume
    max_volume = get_volume(L)

    # Print the result
    print(max_volume)

if __name__ == '__main__':
    main()

