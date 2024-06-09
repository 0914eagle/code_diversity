
def solve(r, c, cake):
    # Initialize a 2D array to store the number of evil strawberries in each row and column
    rows = [[0] * c for _ in range(r)]
    cols = [[0] * c for _ in range(c)]

    # Count the number of evil strawberries in each row and column
    for i in range(r):
        for j in range(c):
            if cake[i][j] == 'S':
                rows[i][j] = 1
                cols[j][i] = 1

    # Find the maximum number of cake cells that can be eaten by choosing a row or column with no evil strawberries
    max_cells = 0
    for i in range(r):
        for j in range(c):
            if rows[i][j] == 0 and cols[j][i] == 0:
                max_cells = max(max_cells, sum(rows[i]) + sum(cols[j]))

    return max_cells

