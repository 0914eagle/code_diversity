
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers that should stay or move from one city to another
    dp = [[0] * n for _ in range(n)]

    # Loop through each city and its neighbors
    for i in range(n):
        for j in range(n):
            # If the current city is the same as the neighboring city, set the number of soldiers to stay to the current number of soldiers
            if i == j:
                dp[i][j] = a[i]
            # If the current city is not the same as the neighboring city, set the number of soldiers to move to the minimum number of soldiers that can be moved
            else:
                dp[i][j] = min(a[i], a[j])

    # Loop through each city and its neighbors
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If the current city is the same as the neighboring city, skip this iteration
                if i == j:
                    continue
                # If the current city is not the same as the neighboring city, check if the number of soldiers that should move from the current city to the neighboring city is less than or equal to the number of soldiers that should stay in the current city
                if dp[i][j] <= dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

    # Check if the number of soldiers in each city is equal to the expected number
    for i in range(n):
        if sum(dp[i]) != b[i]:
            return "NO"

    return "YES"

