
def solve(N, M, K, A, B):
    # Sort the books on Desk A and Desk B by their reading time
    A.sort()
    B.sort()
    # Initialize the number of books read to 0
    num_books = 0
    # Initialize the total time spent reading to 0
    total_time = 0
    # Loop until we have read all the books or the total time exceeds K
    while num_books < N + M and total_time <= K:
        # Check if the next book on Desk A is the fastest to read
        if A[num_books] <= B[num_books]:
            # Read the book on Desk A and remove it from the list
            total_time += A.pop(0)
        # Otherwise, read the book on Desk B
        else:
            total_time += B.pop(0)
        # Increment the number of books read
        num_books += 1
    # Return the number of books read
    return num_books

