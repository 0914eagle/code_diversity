
def solve(a, b, x, y):
    # Initialize a dictionary to store the minimum time needed to reach each floor
    # from the a-th floor of A
    dp = {a: 0}

    # Loop through each floor from a to b
    for i in range(a, b + 1):
        # If we have already calculated the minimum time needed to reach this floor,
        # skip it
        if i in dp:
            continue

        # If we are on the b-th floor, return the minimum time needed to reach it
        if i == b:
            return dp[i]

        # Initialize the minimum time needed to reach this floor as infinite
        dp[i] = float("inf")

        # If there is a corridor connecting this floor to the next floor,
        # calculate the minimum time needed to reach the next floor
        if i < b:
            dp[i] = min(dp[i], dp[i + 1] + x)

        # If there is a staircase connecting this floor to the next floor,
        # calculate the minimum time needed to reach the next floor
        if i < b - 1:
            dp[i] = min(dp[i], dp[i + 2] + y)

    # If we reach this point, it means that there is no way to reach the b-th floor,
    # so return -1
    return -1

