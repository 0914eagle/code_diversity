
def solve(m, n, t):
    # Convert the input parameters to integers
    m = int(m)
    n = int(n)
    t = int(t)

    # Create a dictionary to map the time complexity to the corresponding operation count
    time_complexity = {1: n!, 2: 2^n, 3: n^4, 4: n^3, 5: n^2, 6: n*log2(n), 7: n}

    # Calculate the operation count for the given time complexity and input size
    operation_count = time_complexity[t](n)

    # Check if the operation count is less than or equal to the maximum number of operations per second
    if operation_count <= m:
        return "AC"
    else:
        return "TLE"

