
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    
    # Initialize the number of hidden students in each room
    hidden = [0] * (n + 1)
    
    # Loop through each room
    for i in range(1, n + 1):
        # Check if the current room has any students
        if a[i] > 0:
            # Add the number of students in the current room to the total number of students
            students[i] += a[i]
        
        # Check if the current room has any hidden students
        if hidden[i] > 0:
            # Subtract the number of hidden students in the current room from the total number of students
            students[i] -= hidden[i]
        
        # Check if the current room has non-hidden students different from b
        if students[i] != b:
            # Increment the number of rooms with non-hidden students different from b
            x += 1
    
    # Return the minimum number of rooms with non-hidden students different from b
    return x

