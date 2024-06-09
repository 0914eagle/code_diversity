
def solve(n, a):
    # Initialize the number of shots required to knock each can down to infinity
    shots = [float('inf')] * n
    # Initialize the order of cans to knock down
    order = [0] * n
    # Set the first can to be knocked down with the first shot
    shots[0] = 1
    order[0] = 1
    # Loop through the remaining cans
    for i in range(1, n):
        # Find the can with the minimum number of shots required to knock it down
        min_shots = float('inf')
        for j in range(i):
            if shots[j] + a[j] < min_shots:
                min_shots = shots[j] + a[j]
                k = j
        # Set the number of shots required to knock the current can down
        shots[i] = min_shots
        # Set the order of cans to knock down
        order[i] = k + 1
    # Return the total number of shots required and the order of cans to knock down
    return sum(shots), order

