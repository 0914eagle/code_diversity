
def max_large_bouquets(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the number of large bouquets to 0
    large_bouquets = 0
    
    # Iterate through the array
    for i in range(n):
        # Check if the current flower count is odd
        if a[i] % 2 == 1:
            # Increment the number of large bouquets
            large_bouquets += 1
        # Check if the current flower count is even and there are still flowers left in the array
        elif a[i] % 2 == 0 and i + 1 < n:
            # Combine the current flower count with the next flower count if it is also even
            a[i] += a[i + 1]
            # Remove the next flower count from the array
            a.pop(i + 1)
            # Decrement the number of flowers in the array
            n -= 1
    
    # Return the number of large bouquets
    return large_bouquets

