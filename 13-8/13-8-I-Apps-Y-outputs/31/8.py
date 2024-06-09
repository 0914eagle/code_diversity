
def max_books(desk_a, desk_b, time_limit):
    # Sort the books on both desks by their reading time
    desk_a.sort()
    desk_b.sort()
    
    # Initialize variables to keep track of the current book and time
    current_book_a = 0
    current_book_b = 0
    current_time = 0
    
    # Initialize a variable to keep track of the maximum number of books read
    max_books_read = 0
    
    # Loop until we reach the time limit or one of the desks is empty
    while current_time < time_limit and current_book_a < len(desk_a) and current_book_b < len(desk_b):
        # Check if the current book on Desk A is the fastest to read
        if desk_a[current_book_a] < desk_b[current_book_b]:
            # Read the current book on Desk A and update the time
            current_time += desk_a[current_book_a]
            current_book_a += 1
        # Check if the current book on Desk B is the fastest to read
        elif desk_a[current_book_a] > desk_b[current_book_b]:
            # Read the current book on Desk B and update the time
            current_time += desk_b[current_book_b]
            current_book_b += 1
        # If the books are the same, read the current book on Desk A and update the time
        else:
            current_time += desk_a[current_book_a]
            current_book_a += 1
            current_book_b += 1
        
        # Update the maximum number of books read
        max_books_read += 1
    
    # Return the maximum number of books read
    return max_books_read

