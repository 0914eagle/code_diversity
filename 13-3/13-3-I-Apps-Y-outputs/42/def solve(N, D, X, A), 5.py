
def solve(N, D, X, A):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum(A)
    
    # Calculate the number of chocolate pieces left over at the end of the camp
    left_over = X
    
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    prepared = left_over + total_eaten
    
    return prepared

