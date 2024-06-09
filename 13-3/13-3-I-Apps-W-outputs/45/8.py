
def max_large_bouquets(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    # Initialize the number of large bouquets to 0
    large_bouquets = 0
    # Initialize the total number of flowers in the large bouquets to 0
    total_flowers = 0
    # Iterate through the array
    for i in range(n):
        # Check if the total number of flowers in the large bouquets is odd
        if total_flowers % 2 == 1:
            # If the total number of flowers is odd, we can form a large bouquet with the current bouquet
            large_bouquets += 1
            # Add the number of flowers in the current bouquet to the total number of flowers in the large bouquets
            total_flowers += a[i]
        # If the total number of flowers is even, we cannot form a large bouquet with the current bouquet
        else:
            # Break the loop
            break
    # Return the maximum number of large bouquets that can be formed
    return large_bouquets

