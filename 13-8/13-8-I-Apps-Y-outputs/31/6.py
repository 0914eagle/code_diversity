
def max_books_read(desk_a, desk_b, time_limit):
    # Sort the books on both desks by their reading time
    desk_a.sort(reverse=True)
    desk_b.sort(reverse=True)
    
    # Initialize variables to keep track of the current time and number of books read
    current_time = 0
    num_books_read = 0
    
    # Loop through the books on both desks and read the book with the minimum reading time
    while current_time < time_limit and desk_a and desk_b:
        if desk_a[0] < desk_b[0]:
            current_time += desk_a.pop(0)
        else:
            current_time += desk_b.pop(0)
        num_books_read += 1
    
    # Return the number of books read
    return num_books_read

