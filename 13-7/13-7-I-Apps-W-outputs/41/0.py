
def solve(n):
    # Initialize the array a
    a = list(range(1, n+1))
    # Initialize the number of pairs
    q = 0
    # Loop through each pair of indices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Check if the array has at most two different numbers
            if len(set(a)) <= 2:
                # If the condition is met, add the pair to the list of pairs
                q += 1
                print(i, j)
                # Break out of the inner loop
                break
            # Assign t to be the result of the function f
            t = f(a[i], a[j])
            # Assign a[i] and a[j] to be t
            a[i] = t
            a[j] = t
    return q

# Define the function f
def f(x, y):
    return x + y

