
def solve(n, a):
    # Initialize the minimum number of shots required to knock down each can to infinity
    min_shots = [float('inf')] * n
    # Initialize the order of cans to knock down
    order = [0] * n
    # Initialize the number of shots required to knock down each can to 0
    shots = [0] * n

    # Loop through each can
    for i in range(n):
        # If the current can has not been knocked down yet
        if min_shots[i] == float('inf'):
            # Set the minimum number of shots required to knock down this can to the current number of shots
            min_shots[i] = shots[i]
            # Set the order of cans to knock down to the current can
            order[i] = i + 1

        # Loop through each can that has not been knocked down yet
        for j in range(i + 1, n):
            # If the current can has not been knocked down yet and the minimum number of shots required to knock it down is greater than the current number of shots
            if min_shots[j] > shots[i]:
                # Set the minimum number of shots required to knock down this can to the current number of shots
                min_shots[j] = shots[i]
                # Set the order of cans to knock down to the current can
                order[j] = i + 1

        # Add the durability of the current can to the number of shots required to knock down each can
        shots = [x + a[i] for x in shots]

    # Return the minimum number of shots required to knock down each can and the order of cans to knock down
    return min_shots, order

