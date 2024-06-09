
def get_max_volume(L):
    # Initialize variables
    max_volume = 0
    a = 0
    b = 0
    c = 0
    
    # Iterate through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            for k in range(1, L + 1):
                # Calculate the volume of the current cuboid
                volume = i * j * k
                
                # Check if the volume is greater than the current maximum volume
                if volume > max_volume:
                    max_volume = volume
                    a = i
                    b = j
                    c = k
    
    # Return the maximum volume and the dimensions of the cuboid
    return max_volume, a, b, c

def main():
    # Read the input from stdin
    L = int(input())
    
    # Call the function to get the maximum volume and dimensions of the cuboid
    max_volume, a, b, c = get_max_volume(L)
    
    # Print the output to stdout
    print(max_volume)

if __name__ == '__main__':
    main()

