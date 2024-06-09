
def solve(m, n, t):
    # Convert the input parameters to integers
    m = int(m)
    n = int(n)
    t = int(t)

    # Create a dictionary to map the algorithm complexity to its corresponding operation count
    complexity_dict = {1: n!, 2: 2^n, 3: n^4, 4: n^3, 5: n^2, 6: n*log2(n), 7: n}

    # Calculate the operation count for the given algorithm complexity and input size
    operation_count = complexity_dict[t](n)

    # Check if the operation count is less than or equal to the maximum number of operations that can be performed in one second (m)
    if operation_count <= m:
        return "AC"
    else:
        return "TLE"

