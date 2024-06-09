
def solve(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if it is possible to make all elements equal to k in some number of operations
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j] and a[i] != k and a[j] != k:
                return "no"
    
    return "yes"

