
def get_maximal_comfort(n, a):
    # Sort the array of city codes
    a.sort()
    # Initialize the total comfort to 0
    total_comfort = 0
    # Iterate through the array of city codes
    for i in range(n):
        # Calculate the comfort for the current segment
        comfort = a[i] ^ a[i+1]
        # Add the comfort to the total comfort
        total_comfort += comfort
    # Return the total comfort
    return total_comfort

