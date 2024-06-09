
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers moving from one city to another
    moves = [[0] * n for _ in range(n)]

    # Loop through each road and update the number of soldiers moving from one city to another
    for road in roads:
        moves[road[0] - 1][road[1] - 1] += 1
        moves[road[1] - 1][road[0] - 1] += 1

    # Loop through each city and check if the number of soldiers after roaming is equal to b_i
    for i in range(n):
        total = a[i]
        for j in range(n):
            if i != j:
                total += moves[i][j]
        if total != b[i]:
            return "NO"

    # If all cities have the correct number of soldiers after roaming, return the moves matrix
    return "YES\n" + "\n".join([" ".join(map(str, row)) for row in moves])

