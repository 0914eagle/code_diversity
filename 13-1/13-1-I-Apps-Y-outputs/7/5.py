
import math

def get_max_volume(L):
    # Initialize the variables to brute force
    a = b = c = 1
    max_volume = 0
    
    # Loop through all possible combinations of a, b, and c
    while a <= L:
        while b <= L - a:
            c = L - a - b
            if c >= 0:
                # Calculate the volume of the current cuboid
                volume = a * b * c
                
                # Check if the volume is greater than the current maximum volume
                if volume > max_volume:
                    max_volume = volume
            
            # Increment b to get the next combination
            b += 1
        
        # Reset b and increment a to get the next combination
        b = 1
        a += 1
    
    # Return the maximum volume
    return max_volume

