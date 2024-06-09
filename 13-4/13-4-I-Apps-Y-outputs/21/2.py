
def solve(m, n, t):
    # Convert the input parameters to integers
    m = int(m)
    n = int(n)
    t = int(t)

    # Create a dictionary to map the algorithm complexity to the number of operations
    complexity_dict = {1: 1, 2: 2, 3: 4, 4: 9, 5: 16, 6: 25, 7: 36}

    # Calculate the number of operations for the given algorithm complexity and input size
    num_operations = complexity_dict[t] * n

    # Check if the number of operations is less than or equal to the maximum number of operations per second
    if num_operations <= m:
        return "AC"
    else:
        return "TLE"

