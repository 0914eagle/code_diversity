
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    
    # Initialize the number of hidden students in each room
    hidden = [0] * (n + 1)
    
    # Loop through each room
    for i in range(1, n + 1):
        # If the number of students in the current room is different from b
        if a[i] != b:
            # Increment the number of rooms with non-hidden students different from b
            x += 1
        
        # If the current room is not the last room
        if i != n:
            # Loop through each student in the current room
            for j in range(a[i]):
                # If the student can run to the next room
                if d >= 1:
                    # Decrement the number of students in the current room
                    a[i] -= 1
                    # Increment the number of students in the next room
                    a[i + 1] += 1
                    # Decrement the running distance of the student
                    d -= 1
                # If the student cannot run to the next room
                else:
                    # Increment the number of hidden students in the current room
                    hidden[i] += 1
    
    # Return the minimum number of rooms with non-hidden students different from b
    return x

