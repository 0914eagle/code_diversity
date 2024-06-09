
def solve(n):
    # Initialize the array a
    a = list(range(1, n+1))
    # Initialize the number of pairs
    q = 0
    # Loop through each pair of indices
    for i in range(1, n):
        for j in range(i+1, n+1):
            # Check if the array already has at most two different numbers
            if len(set(a)) <= 2:
                # If so, break the loop
                break
            # Otherwise, perform the operation
            t = f(a[i], a[j])
            a[i] = t
            a[j] = t
            # Increment the number of pairs
            q += 1
    # Return the list of pairs
    return q, [(i, j) for i in range(1, n) for j in range(i+1, n+1) if f(a[i], a[j]) != a[i]]

