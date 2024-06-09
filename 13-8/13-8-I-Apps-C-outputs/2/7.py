
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x_1 = 0
    x_2 = 0
    
    # Iterate through each room
    for i in range(n):
        # Calculate the number of students in the current room
        students = a[i]
        
        # If the number of students is different from b, increment the appropriate counter
        if students != b:
            if i % 2 == 0:
                x_1 += 1
            else:
                x_2 += 1
    
    # Return the minimal possible value of the maximum of x_i
    return min(x_1, x_2)

