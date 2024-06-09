
def solve(n, a):
    # Initialize the minimum value and its corresponding indices
    min_val = float('inf')
    i, j = 0, 0
    
    # Iterate over all pairs of indices
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the value of the function for the current pair of indices
            val = (i - j) ** 2 + g(i, j, a) ** 2
            
            # If the value is less than the minimum value, update the minimum value and its corresponding indices
            if val < min_val:
                min_val = val
                i, j = i, j
    
    # Return the minimum value
    return min_val

def g(i, j, a):
    # Initialize the sum
    sum = 0
    
    # Iterate over the elements between the two indices
    for k in range(min(i, j) + 1, max(i, j)):
        sum += a[k]
    
    # Return the sum
    return sum

