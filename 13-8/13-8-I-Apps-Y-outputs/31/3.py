
def read_books(N, M, K, A, B):
    # Sort the books on Desk A and Desk B by their reading time
    A.sort()
    B.sort()
    
    # Initialize the number of books read to 0
    books_read = 0
    
    # Initialize the time taken to read the books to 0
    time_taken = 0
    
    # Loop through the books on Desk A and Desk B
    while A and B:
        # Check if the time taken to read the books so far is less than or equal to the given time limit
        if time_taken <= K:
            # Add the time taken to read the topmost book on Desk A to the time taken
            time_taken += A[0]
            # Remove the topmost book from Desk A
            A.pop(0)
            # Increment the number of books read
            books_read += 1
        if time_taken <= K:
            # Add the time taken to read the topmost book on Desk B to the time taken
            time_taken += B[0]
            # Remove the topmost book from Desk B
            B.pop(0)
            # Increment the number of books read
            books_read += 1
    
    # Return the maximum number of books that can be read within the given time limit
    return books_read

