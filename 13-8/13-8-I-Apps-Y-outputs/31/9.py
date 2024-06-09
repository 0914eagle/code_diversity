
def read_books(desk_a, desk_b, time_limit):
    # Sort the books on both desks by reading time
    desk_a.sort(key=lambda x: x[1])
    desk_b.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the current desk and time
    current_desk = 0
    current_time = 0
    books_read = 0
    
    # Loop through the desks until we reach the time limit or one of the desks is empty
    while current_time < time_limit and (desk_a or desk_b):
        # Check if the current desk has any books remaining
        if desk_a and desk_b:
            # If both desks have books remaining, check which desk has the shortest reading time
            if desk_a[0][1] < desk_b[0][1]:
                current_desk = 0
            else:
                current_desk = 1
        elif desk_a:
            # If only desk A has books remaining, set the current desk to desk A
            current_desk = 0
        else:
            # If only desk B has books remaining, set the current desk to desk B
            current_desk = 1
        
        # Read the topmost book on the current desk and remove it from the desk
        current_time += desk_a[0][1] if current_desk == 0 else desk_b[0][1]
        desk_a.pop(0) if current_desk == 0 else desk_b.pop(0)
        books_read += 1
    
    # Return the number of books read
    return books_read

