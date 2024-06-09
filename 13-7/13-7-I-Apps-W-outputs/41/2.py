
def solve(n):
    # Initialize the array a with the numbers 1 to n
    a = list(range(1, n+1))
    # Initialize the number of pairs q to 0
    q = 0
    # Iterate through all possible pairs of numbers
    for x in range(1, n+1):
        for y in range(x+1, n+1):
            # Check if the pair (x, y) satisfies the condition
            if f(a[x-1], a[y-1]) == f(a[y-1], a[x-1]):
                # If the pair satisfies the condition, add it to the list of pairs
                q += 1
                print(x, y)
    return q

