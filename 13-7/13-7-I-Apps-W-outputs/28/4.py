
def get_maximum_total_comfort(N, A):
    # Sort the friendliness of the players in non-decreasing order
    sorted_A = sorted(A)

    # Initialize the total comfort to 0
    total_comfort = 0

    # Loop through each player and calculate their comfort
    for i in range(N):
        # If the player is not the first player to arrive, calculate their comfort based on the friendliness of the clockwise and counter-clockwise adjacent players
        if i > 0:
            clockwise_comfort = min(sorted_A[i-1], sorted_A[i])
            counter_clockwise_comfort = min(sorted_A[i], sorted_A[i-1])
            comfort = clockwise_comfort + counter_clockwise_comfort
        # If the player is the first player to arrive, their comfort is 0
        else:
            comfort = 0

        # Add the comfort of the current player to the total comfort
        total_comfort += comfort

    # Return the maximum total comfort
    return total_comfort

