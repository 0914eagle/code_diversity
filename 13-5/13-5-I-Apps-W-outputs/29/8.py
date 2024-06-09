
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers that should stay or move from one city to another
    dp = [[0] * n for _ in range(n)]

    # Loop through each city and its neighbors
    for i in range(n):
        for j in range(n):
            # If the city is not connected to its neighbor, continue to the next neighbor
            if i == j or (i, j) not in roads:
                continue

            # Calculate the number of soldiers that should move from city i to city j
            dp[i][j] = max(0, dp[i][j] + dp[i][i] - a[i])

            # Calculate the number of soldiers that should stay in city i
            dp[i][i] = max(0, dp[i][i] - a[i])

    # Check if the conditions can be met
    for i in range(n):
        if dp[i][i] != b[i]:
            return "NO"

    # If the conditions can be met, return the solution
    return "YES" + "\n" + "\n".join(" ".join(map(str, row)) for row in dp)

