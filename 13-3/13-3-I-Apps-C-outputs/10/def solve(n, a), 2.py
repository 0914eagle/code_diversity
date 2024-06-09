
def solve(n, a):
    # Initialize the minimum value and its corresponding indices
    min_val = float('inf')
    i, j = 0, 0
    
    # Iterate over all pairs of indices
    for i in range(1, n+1):
        for j in range(1, n+1):
            # Calculate the value of f(i, j)
            val = (i-j)**2 + g(i, j, a)**2
            
            # If the value is less than the minimum, update the minimum and its indices
            if val < min_val:
                min_val = val
                i, j = i, j
    
    return min_val

def g(i, j, a):
    # Calculate the sum of the elements between the two indices
    sum = 0
    for k in range(min(i, j)+1, max(i, j)+1):
        sum += a[k]
    
    return sum

