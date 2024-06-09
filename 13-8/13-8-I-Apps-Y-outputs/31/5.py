
def read_books(N, M, K, A, B):
    # Sort the books on Desk A and Desk B by their reading times
    A.sort()
    B.sort()
    
    # Initialize variables to keep track of the current time and the number of books read
    current_time = 0
    num_books_read = 0
    
    # Loop through the books on Desk A and Desk B
    while A and B and current_time < K:
        # Choose the desk with the book that can be read the soonest
        if A[0] < B[0]:
            # Read the topmost book on Desk A and remove it from the desk
            current_time += A.pop(0)
            num_books_read += 1
        else:
            # Read the topmost book on Desk B and remove it from the desk
            current_time += B.pop(0)
            num_books_read += 1
    
    # Return the maximum number of books that can be read within the given time limit
    return num_books_read

