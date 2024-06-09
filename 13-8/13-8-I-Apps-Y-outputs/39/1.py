
def pistol_shooting(n, durability):
    # Initialize the number of shots required to knock down each can to infinity
    shots_required = [float('inf')] * n
    # Initialize the order of cans to knock down
    order = []
    # Loop through each can and calculate the minimum number of shots required to knock it down
    for i in range(n):
        # If the can has already been knocked down, continue to the next can
        if shots_required[i] != float('inf'):
            continue
        # Calculate the minimum number of shots required to knock down the current can
        shots_required[i] = sum(durability[:i]) + 1
        # Add the current can to the order of cans to knock down
        order.append(i + 1)
    # Return the minimum number of shots required to knock down each can and the order of cans to knock down
    return sum(shots_required), order

