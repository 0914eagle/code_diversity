
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x_1 = 0
    x_2 = 0
    
    # Loop through each room
    for i in range(n):
        # Check if the number of students in the room is different from b
        if a[i] != b:
            # Increment the number of rooms with non-hidden students different from b
            x_1 += 1
            x_2 += 1
        # Check if the room is being processed by the second instructor
        if i % 2 == 0:
            # Decrement the number of rooms with non-hidden students different from b
            x_2 -= 1
    
    # Return the minimum value of the maximum of x_i
    return min(x_1, x_2)
