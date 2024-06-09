
def collatz_conjecture(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()

    # Iterate through the sequence
    for i in range(n):
        # Calculate the value of f for the current element
        f_value = gcd(a[i], a[i+1], a[i+2], a[i+3])

        # Add the value of f to the set of distinct values
        distinct_values.add(f_value)

    # Return the number of distinct values of f
    return len(distinct_values)

