
import math

def get_volume(l):
    
    # Initialize the maximum volume
    max_volume = 0

    # Loop through all possible combinations of dimensions
    for a in range(1, l + 1):
        for b in range(1, l + 1):
            for c in range(1, l + 1):
                # Calculate the volume of the current cuboid
                volume = a * b * c

                # Check if the volume is greater than the maximum volume
                if volume > max_volume:
                    max_volume = volume

    return max_volume

def main():
    
    # Read the input from stdin
    l = int(input())

    # Calculate the maximum possible volume
    volume = get_volume(l)

    # Print the output to stdout
    print(volume)

if __name__ == '__main__':
    main()

