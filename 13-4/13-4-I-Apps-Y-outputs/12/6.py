
import math

def get_volume(l):
    
    # Initialize the volume to 0
    volume = 0

    # Loop through all possible combinations of dimensions
    for a in range(1, l + 1):
        for b in range(1, l + 1):
            for c in range(1, l + 1):
                # Check if the sum of the dimensions is equal to L
                if a + b + c == l:
                    # Calculate the volume of the current cuboid
                    volume = max(volume, a * b * c)

    return volume

def main():
    # Read the input from stdin
    l = int(input())

    # Calculate the maximum possible volume of the rectangular cuboid
    volume = get_volume(l)

    # Print the output to stdout
    print(volume)

if __name__ == '__main__':
    main()

