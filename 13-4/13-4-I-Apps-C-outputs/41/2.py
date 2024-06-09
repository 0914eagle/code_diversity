
def get_max_value(a, k):
    n = len(a)
    if k >= n:
        return sum(a)
    
    # Sort the array to get the maximum sum
    a.sort()
    
    # Initialize the maximum sum and the number of swaps used
    max_sum = 0
    swaps_used = 0
    
    # Loop through the array and find the maximum sum while using at most k swaps
    for i in range(n):
        if swaps_used >= k:
            break
        max_sum += a[i]
        swaps_used += 1
    
    return max_sum

