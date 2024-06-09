
import math

def get_max_volume(L):
    # Initialize the maximum volume to 0
    max_volume = 0
    
    # Loop through all possible values of a, b, and c
    for a in range(1, L + 1):
        for b in range(1, L + 1):
            for c in range(1, L + 1):
                # Calculate the volume of the current cuboid
                volume = a * b * c
                
                # Check if the volume is greater than the maximum volume
                if volume > max_volume:
                    max_volume = volume
    
    # Return the maximum volume
    return max_volume

