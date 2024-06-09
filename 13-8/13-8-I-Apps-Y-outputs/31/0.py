
def read_books(desk_a, desk_b, time_limit):
    # Sort the books on both desks by their reading time
    desk_a.sort(key=lambda x: x[1])
    desk_b.sort(key=lambda x: x[1])
    
    # Initialize variables to keep track of the current desk, time elapsed, and books read
    current_desk = 0
    time_elapsed = 0
    books_read = 0
    
    # Loop until we reach the time limit or we have read all the books
    while time_elapsed < time_limit and books_read < len(desk_a) + len(desk_b):
        # If we are currently reading from Desk A, read the topmost book and remove it from the desk
        if current_desk == 0:
            time_elapsed += desk_a[0][1]
            desk_a.pop(0)
        # If we are currently reading from Desk B, read the topmost book and remove it from the desk
        else:
            time_elapsed += desk_b[0][1]
            desk_b.pop(0)
        
        # Update the current desk and the number of books read
        current_desk = 1 - current_desk
        books_read += 1
    
    # Return the number of books read
    return books_read

