
def get_max_volume(L):
    
    # Initialize the variables to find the maximum volume
    a = b = c = 0
    max_volume = 0

    # Loop through all possible combinations of a, b, and c
    for i in range(1, L + 1):
        for j in range(1, L + 1 - i):
            for k in range(1, L + 1 - i - j):
                # Calculate the volume of the current cuboid
                volume = i * j * k

                # Check if the current volume is greater than the maximum volume
                if volume > max_volume:
                    max_volume = volume
                    a = i
                    b = j
                    c = k

    # Return the maximum volume
    return max_volume

