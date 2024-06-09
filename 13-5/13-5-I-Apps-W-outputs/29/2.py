
def solve(n, m, a, b, roads):
    # Initialize a matrix to store the number of soldiers moving from one city to another
    matrix = [[0] * n for _ in range(n)]

    # Populate the matrix with the number of soldiers moving from one city to another
    for p, q in roads:
        matrix[p - 1][q - 1] = 1
        matrix[q - 1][p - 1] = 1

    # Check if the conditions can be met
    for i in range(n):
        # Calculate the total number of soldiers moving into city i
        total_moving_in = sum(matrix[i])

        # Calculate the total number of soldiers moving out of city i
        total_moving_out = sum(matrix[i][j] for j in range(n) if j != i)

        # Check if the number of soldiers in city i after roaming is correct
        if total_moving_in - total_moving_out != b[i]:
            return "NO"

    # If all conditions are met, return the matrix
    return "YES\n" + "\n".join(" ".join(str(x) for x in row) for row in matrix)

