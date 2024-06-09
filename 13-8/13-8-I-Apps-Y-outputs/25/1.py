
def solve(N, D, X, A):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum([(i * (A[i-1] + 1)) for i in range(1, N+1)])
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    prepared = X + total_eaten
    return prepared

