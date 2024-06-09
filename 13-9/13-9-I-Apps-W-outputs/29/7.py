
def solve(n, a, b):
    # Sort the results in ascending order
    a.sort()
    b.sort()
    
    # Initialize the finalists string
    finalists = "0" * n
    
    # Determine the k value based on the results
    k = 0
    while k < n and a[k] <= b[k]:
        k += 1
    
    # Update the finalists string based on the k value
    for i in range(k):
        finalists = finalists[:i] + "1" + finalists[i+1:]
    
    return finalists

