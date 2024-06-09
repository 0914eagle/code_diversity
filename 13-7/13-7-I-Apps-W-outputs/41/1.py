
def solve(n):
    # Initialize the array a with the values 1, 2, ..., n
    a = list(range(1, n+1))
    # Initialize the number of pairs q to 0
    q = 0
    # Loop through each pair of indices i and j
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Check if the array a has at most two different numbers
            if len(set(a)) <= 2:
                # If the array a has at most two different numbers, break the loop
                break
            # Otherwise, increment the number of pairs q
            q += 1
            # Perform the operation on the pair (i, j)
            t = f(a[i], a[j])
            a[i] = t
            a[j] = t
    # Return the list of pairs
    return q, [(i, j) for i in range(1, n+1) for j in range(i+1, n+1) if f(a[i], a[j]) != a[i]]

# Define the function f(x, y) to be the maximum of x and y
def f(x, y):
    return max(x, y)

# Test the function with the example input n = 3
n = 3
q, pairs = solve(n)
print(q)
for pair in pairs:
    print(*pair)

# Test the function with the example input n = 4
n = 4
q, pairs = solve(n)
print(q)
for pair in pairs:
    print(*pair)

