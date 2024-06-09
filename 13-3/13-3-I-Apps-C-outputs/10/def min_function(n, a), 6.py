
def min_function(n, a):
    # Initialize the minimum value and its indices
    min_val = float('inf')
    i, j = 0, 0
    
    # Iterate over all pairs of indices
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Calculate the value of the function at (i, j)
            val = (i - j) ** 2 + g(i, j, a) ** 2
            
            # If the value is less than the minimum, update the minimum and its indices
            if val < min_val:
                min_val = val
                i, j = i, j
    
    return min_val

def g(i, j, a):
    # Calculate the sum of the elements between i and j (inclusive)
    sum = sum(a[i:j + 1])
    return sum

