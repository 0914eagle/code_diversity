
def solve(n, d, x, a):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum(a)
    
    # Calculate the number of chocolate pieces remaining at the end of the camp
    remaining = x
    
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    prepared = remaining - total_eaten
    
    return prepared

