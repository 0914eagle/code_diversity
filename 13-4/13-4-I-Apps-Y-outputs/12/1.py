
def get_volume(L):
    # Initialize variables
    volume = 0
    a = 0
    b = 0
    c = 0
    
    # Loop through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            for k in range(1, L + 1):
                # Check if the sum of a, b, and c is equal to L
                if i + j + k == L:
                    # Calculate the volume of the rectangular cuboid
                    volume = i * j * k
                    # Check if the volume is greater than the current maximum volume
                    if volume > max_volume:
                        # Update the maximum volume and the dimensions of the rectangular cuboid
                        max_volume = volume
                        a = i
                        b = j
                        c = k
    
    # Return the maximum volume and the dimensions of the rectangular cuboid
    return max_volume, a, b, c

def main():
    # Read the input from stdin
    L = int(input())
    
    # Call the get_volume function and print the result
    max_volume, a, b, c = get_volume(L)
    print(max_volume)
    
if __name__ == '__main__':
    main()

