
def solve(n, d, b, a):
    # Initialize the number of rooms with non-hidden students different from b
    x = 0
    
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    
    # Initialize the number of hidden students in each room
    hidden = [0] * (n + 1)
    
    # Initialize the current room number
    current_room = 1
    
    # Loop through each room
    for i in range(n):
        # If the current room is not the last room
        if current_room != n:
            # Add the number of students in the current room to the total number of students
            students[current_room] += a[current_room]
            
            # If the number of students in the current room is different from the official number of students
            if a[current_room] != b:
                # Increment the number of rooms with non-hidden students different from b
                x += 1
            
            # If the current room is not the first room
            if current_room != 1:
                # Add the number of hidden students in the previous room to the total number of hidden students
                hidden[current_room - 1] += hidden[current_room]
            
            # Move to the next room
            current_room += 1
        # If the current room is the last room
        else:
            # Add the number of students in the current room to the total number of students
            students[current_room] += a[current_room]
            
            # If the number of students in the current room is different from the official number of students
            if a[current_room] != b:
                # Increment the number of rooms with non-hidden students different from b
                x += 1
            
            # Move to the first room
            current_room = 1
    
    # Return the minimum number of rooms with non-hidden students different from b
    return x

