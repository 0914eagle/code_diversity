
def solve(n):
    # Initialize the array a
    a = list(range(1, n+1))
    # Initialize the number of pairs
    q = 0
    # Loop through each pair of numbers
    for i in range(1, n):
        for j in range(i+1, n+1):
            # Check if the pair is valid
            if a[i] != a[j]:
                # Increment the number of pairs
                q += 1
                # Print the pair
                print(i, j)
                # Break the loop
                break
    # Return the number of pairs
    return q

