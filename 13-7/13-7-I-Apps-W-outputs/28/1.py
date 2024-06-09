
def solve(N, A):
    # Sort the friendliness values in descending order
    A.sort(reverse=True)
    # Initialize the total comfort to 0
    total_comfort = 0
    # Loop through the players and calculate their comfort
    for i in range(N):
        # If it is the first player, they get no comfort
        if i == 0:
            comfort = 0
        # Otherwise, calculate the comfort as the minimum of the clockwise and counter-clockwise adjacent players
        else:
            comfort = min(A[i-1], A[i])
        # Add the comfort to the total comfort
        total_comfort += comfort
    # Return the total comfort
    return total_comfort

