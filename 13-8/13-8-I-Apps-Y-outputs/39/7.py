
def can_shooting(n, a):
    # Sort the cans in non-decreasing order of their durability
    sorted_cans = sorted(enumerate(a), key=lambda x: x[1])

    # Initialize the minimum number of shots required to knock down all cans
    min_shots = 0

    # Initialize the order of cans to shoot in
    order = []

    # Loop through each can in non-decreasing order of their durability
    for i, can in sorted_cans:
        # Add the current can to the order
        order.append(i)

        # Calculate the number of shots required to knock down the current can
        shots = sum(a[j] * (j < i) for j in range(n)) + 1

        # Update the minimum number of shots required to knock down all cans
        min_shots += shots

    return min_shots, order

