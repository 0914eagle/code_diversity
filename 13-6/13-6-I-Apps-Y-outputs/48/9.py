
def sock_washing(S, C, K, D):
    # Sort the socks by their color values
    D.sort()
    # Initialize the number of machines to 0
    machines = 0
    # Loop through the socks
    for i in range(S):
        # Check if the current sock is too far from the previous sock
        if i > 0 and abs(D[i] - D[i-1]) > K:
            # Increment the number of machines
            machines += 1
        # Check if the current sock is the first sock or if the current machine has reached its capacity
        if i == 0 or (i % C == 0 and i > 0):
            # Increment the number of machines
            machines += 1
    return machines

