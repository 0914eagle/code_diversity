
import math

def get_volume(l):
    
    # Initialize the variables
    x = 0
    y = 0
    z = 0
    volume = 0

    # Loop through all possible combinations of x, y, and z
    for i in range(1, l + 1):
        for j in range(1, l + 1):
            for k in range(1, l + 1):
                # Check if the current combination is a valid solution
                if i + j + k == l:
                    # Calculate the volume of the current cuboid
                    volume = i * j * k
                    # Check if the current volume is greater than the previous maximum volume
                    if volume > max_volume:
                        # Update the maximum volume and the corresponding dimensions
                        max_volume = volume
                        x = i
                        y = j
                        z = k

    return max_volume

def main():
    # Read the input from stdin
    l = int(input())

    # Calculate the maximum possible volume of the rectangular cuboid
    volume = get_volume(l)

    # Print the output to stdout
    print(volume)

if __name__ == '__main__':
    main()

