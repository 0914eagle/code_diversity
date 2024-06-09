
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Iterate through each room
    for i in range(n):
        # If the number of students in the room is not equal to b, increment x
        if a[i] != b:
            x += 1
    
    # Return the minimum possible value of x
    return x

