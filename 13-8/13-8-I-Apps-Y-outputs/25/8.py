
def solve(n, d, x, *a):
    # Calculate the total number of chocolate pieces eaten by all participants
    total_eaten = sum([(i // (d - i % d) + 1) * a[i % n] for i in range(n)])
    # Calculate the number of chocolate pieces prepared at the beginning of the camp
    return x + total_eaten

