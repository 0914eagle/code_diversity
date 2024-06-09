
def solve(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()

    # Iterate over the given sequence
    for i in range(n):
        # Calculate the value of f for the current element
        f_value = 1
        for j in range(i+1, n):
            f_value = gcd(f_value, a[j])

        # Add the value of f to the set of distinct values
        distinct_values.add(f_value)

    # Return the number of distinct values of f
    return len(distinct_values)

