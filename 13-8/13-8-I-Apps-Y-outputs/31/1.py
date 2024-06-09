
def solve(N, M, K, A, B):
    # Sort the books on Desk A and Desk B by their reading time
    A.sort()
    B.sort()
    
    # Initialize variables to keep track of the number of books read and the total time taken
    num_books = 0
    total_time = 0
    
    # Loop through the books on Desk A and Desk B
    while num_books < N and num_books < M and total_time < K:
        # If the current book on Desk A is the fastest to read, read it and remove it from the desk
        if A[num_books] < B[num_books]:
            total_time += A.pop(0)
        # If the current book on Desk B is the fastest to read, read it and remove it from the desk
        else:
            total_time += B.pop(0)
        num_books += 1
    
    # Return the maximum number of books that can be read within the given time limit
    return num_books

