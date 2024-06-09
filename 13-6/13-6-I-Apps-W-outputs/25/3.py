
def solve(N, X, M):
    # Initialize the sequence with the given initial value
    A = [X]
    
    # Iterate from 1 to N-1 and calculate the next value of the sequence
    for i in range(1, N):
        A.append(pow(A[i-1], 2, M))
    
    # Return the sum of the first N elements of the sequence
    return sum(A)

