
def solve(N, X, M):
    # Calculate the remainder of Euclidean division of X by M
    remainder = X % M
    
    # Initialize the sum
    sum = 0
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # Calculate the next term of the sequence
        term = remainder ** 2 % M
        
        # Add the term to the sum
        sum += term
        
        # Update the remainder for the next iteration
        remainder = term
    
    # Return the sum
    return sum

