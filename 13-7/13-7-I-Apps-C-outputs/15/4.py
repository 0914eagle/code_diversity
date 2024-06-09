
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x_1 = 0
    x_2 = 0
    
    # Iterate through each room
    for i in range(n):
        # Calculate the number of students in the room
        num_students = a[i]
        
        # If the number of students is different from b, increment the number of rooms with non-hidden students different from b
        if num_students != b:
            x_1 += 1
            x_2 += 1
        
        # If the room is even and the number of students is different from b, increment the number of rooms with non-hidden students different from b
        if i % 2 == 0 and num_students != b:
            x_1 += 1
        
        # If the room is odd and the number of students is different from b, increment the number of rooms with non-hidden students different from b
        if i % 2 == 1 and num_students != b:
            x_2 += 1
    
    # Return the minimum value of the maximum of x_i
    return min(x_1, x_2)

