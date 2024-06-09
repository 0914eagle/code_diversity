
def solve(S, C, K, D):
    # Sort the socks by color
    D.sort()
    # Initialize the number of machines to 0
    machines = 0
    # Iterate through the socks
    for i in range(S):
        # Check if the current sock is within the range of the current machine
        if D[i] - D[i-C] <= K:
            # If it is, increment the machine number
            machines += 1
    # Return the number of machines needed
    return machines

