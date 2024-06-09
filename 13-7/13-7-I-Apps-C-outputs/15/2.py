
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x_1 = 0
    x_2 = 0
    
    # Iterate through each room
    for i in range(n):
        # Calculate the number of students in the room
        num_students = a[i]
        
        # Check if the number of students is different from b
        if num_students != b:
            # Increment the number of rooms with non-hidden students different from b
            x_1 += 1
            x_2 += 1
        
        # If the room is not the first or last room
        if i != 0 and i != n - 1:
            # Calculate the maximum number of rooms that a student can run to
            max_rooms = min(d, n - i - 1)
            
            # Iterate through each possible room that a student can run to
            for j in range(1, max_rooms + 1):
                # Calculate the number of students in the next room
                next_room = i + j
                num_students_next = a[next_room]
                
                # Check if the number of students in the next room is different from b
                if num_students_next != b:
                    # Increment the number of rooms with non-hidden students different from b
                    x_1 += 1
                    x_2 += 1
    
    # Return the minimum of the maximum of x_1 and x_2
    return min(x_1, x_2)

