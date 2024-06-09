
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Iterate through the rooms
    for i in range(n):
        # Check if the current room has any non-hidden students
        if a[i] > b:
            # Increment the number of rooms with non-hidden students different from b
            x += 1
    
    # Return the minimum possible value of the maximum of x_i
    return x

