
def solve(n, q, a):
    # Initialize a dictionary to store the minimum energy released for each atom
    min_energy = {1: 0}
    for i in range(2, n+1):
        min_energy[i] = min(min_energy[j] + a[i-j] for j in range(1, i))
    
    # Return the minimum energy released for each query
    return [min_energy[k] for k in q]

