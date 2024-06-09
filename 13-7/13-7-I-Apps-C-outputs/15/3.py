
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Iterate through each room
    for i in range(n):
        # Check if the number of students in the room is different from b
        if a[i] != b:
            x += 1
    
    # Return the minimum possible value of the maximum of x_i
    return x

