
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x_1 = 0
    x_2 = 0
    
    # Iterate through each room
    for i in range(n):
        # Check if the number of students in the room is different from b
        if a[i] != b:
            # Increment the number of rooms with non-hidden students different from b
            x_1 += 1
            x_2 += 1
    
    # Return the minimum of the maximum of x_1 and x_2
    return min(x_1, x_2)

