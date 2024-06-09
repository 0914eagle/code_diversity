
def solve(N, D, X, A):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum(A)
    
    # Check if the total number of chocolate pieces eaten is equal to the number of pieces remaining at the end of the camp
    if total_eaten == X:
        # If they are equal, then the number of pieces prepared at the beginning of the camp is N - total_eaten
        return N - total_eaten
    else:
        # If they are not equal, then the number of pieces prepared at the beginning of the camp is not determined
        return -1

