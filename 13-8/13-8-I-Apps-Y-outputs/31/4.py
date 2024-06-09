
def read_books(n, m, k, a, b):
    # Sort the books on desk A and desk B by their reading time
    desk_a = sorted(a)
    desk_b = sorted(b)
    
    # Initialize variables to keep track of the number of books read and the time elapsed
    num_books = 0
    time_elapsed = 0
    
    # Loop until we have read all the books or the time limit is reached
    while num_books < n + m and time_elapsed <= k:
        # Check if the next book on desk A is ready to be read
        if desk_a[num_books] <= time_elapsed:
            # Read the book and remove it from the desk
            time_elapsed += desk_a[num_books]
            num_books += 1
        
        # Check if the next book on desk B is ready to be read
        if desk_b[num_books] <= time_elapsed:
            # Read the book and remove it from the desk
            time_elapsed += desk_b[num_books]
            num_books += 1
    
    # Return the number of books read
    return num_books

