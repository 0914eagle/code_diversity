
def get_large_bouquets(n, a):
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
        # If the current flower count is even, combine it with the previous even flower count
        else:
            # Check if the previous flower count is not None
            if a[i-1] is not None:
                # Combine the current and previous flower counts
                a[i-1] += a[i]
                # Set the current flower count to None
                a[i] = None
    
    # Return the number of large bouquets
    return large_bouquets

