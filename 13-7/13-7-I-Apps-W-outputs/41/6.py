
def solve(n):
    # Initialize the array a
    a = list(range(1, n+1))
    # Initialize the number of pairs
    q = 0
    # Loop through each element in the array
    for i in range(n):
        # Find the index of the element that is not i
        j = (i+1) % n
        # Swap the elements at indices i and j
        a[i], a[j] = a[j], a[i]
        # Increment the number of pairs
        q += 1
    # Return the array and the number of pairs
    return a, q

