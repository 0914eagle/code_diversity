
def get_minimum_shots(n, a):
    # Initialize the number of shots required to knock each can down as infinity
    shots = [float('inf')] * n
    # Initialize the order of cans as empty
    order = []
    # Loop through each can
    for i in range(n):
        # If the current can has not been knocked down yet
        if shots[i] == float('inf'):
            # Set the number of shots required to knock the current can down to 1
            shots[i] = 1
            # Add the current can to the order
            order.append(i + 1)
            # Loop through the remaining cans
            for j in range(i + 1, n):
                # If the current can has not been knocked down yet and the number of shots required to knock it down is less than the current minimum
                if shots[j] == float('inf') and shots[i] * a[j] + 1 < shots[j]:
                    # Set the number of shots required to knock the current can down
                    shots[j] = shots[i] * a[j] + 1
                    # Add the current can to the order
                    order.append(j + 1)
    # Return the minimum number of shots required to knock each can down and the order of cans
    return sum(shots), order

