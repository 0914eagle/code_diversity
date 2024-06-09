
def solve(n):
    # Initialize the array a with the values from 1 to n
    a = list(range(1, n+1))
    # Initialize the number of pairs to 0
    q = 0
    # Loop through each pair of indices i and j
    for i in range(n):
        for j in range(i+1, n):
            # Check if the current pair of indices satisfies the condition
            if a[i] != a[j]:
                # If the current pair of indices does not satisfy the condition, continue to the next pair
                continue
            # If the current pair of indices satisfies the condition, increment the number of pairs
            q += 1
            # Print the current pair of indices
            print(i+1, j+1)
    return q

