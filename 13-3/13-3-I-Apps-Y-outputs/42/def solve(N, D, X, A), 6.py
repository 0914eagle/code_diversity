
def solve(N, D, X, A):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum(A)
    
    # Calculate the number of chocolate pieces remaining at the end of the camp
    remaining = X
    
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    prepared = remaining - total_eaten
    
    return prepared

