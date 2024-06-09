
def solve(a, b, x, y):
    # Initialize a dictionary to store the minimum time to reach each floor
    # from the a-th floor of A
    dp = {a: 0}

    # Loop through each floor from a to b
    for i in range(a, b + 1):
        # If we have already calculated the minimum time to reach this floor,
        # skip this iteration
        if i in dp:
            continue

        # If we are at the b-th floor, return the minimum time to reach this floor
        if i == b:
            return dp[i]

        # Initialize the minimum time to reach this floor as infinity
        dp[i] = float("inf")

        # If there is a corridor connecting the i-th floor of A and the (i-1)-th floor of B,
        # calculate the minimum time to reach the (i-1)-th floor of B from the a-th floor of A
        if i - 1 in dp:
            dp[i] = min(dp[i], dp[i - 1] + x)

        # If there is a staircase connecting the i-th floor of A and the (i+1)-th floor of B,
        # calculate the minimum time to reach the (i+1)-th floor of B from the a-th floor of A
        if i + 1 in dp:
            dp[i] = min(dp[i], dp[i + 1] + y)

    # If we have reached the end of the loop and the b-th floor is not in the dictionary,
    # then there is no path from the a-th floor of A to the b-th floor of B
    if b not in dp:
        return -1

    # Return the minimum time to reach the b-th floor of B from the a-th floor of A
    return dp[b]

