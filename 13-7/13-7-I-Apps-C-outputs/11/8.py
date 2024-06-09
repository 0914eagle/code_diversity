
def get_min_energy(n, q, a, k):
    # Initialize a dictionary to store the minimum energy released for each number of neutrons
    min_energy = {1: a[1]}
    for i in range(2, n+1):
        min_energy[i] = min(min_energy[i-1], a[i])
    
    # Loop through the queries and return the minimum energy released for each query
    for k in q:
        if k <= n:
            yield min_energy[k]
        else:
            # Find the largest number of neutrons that can be decomposed from the current atom
            i = 1
            while i * (i+1) // 2 <= k:
                i += 1
            j = k - i * (i-1) // 2
            yield min_energy[i] + min_energy[j]

