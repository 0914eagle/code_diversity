
def solve(game_state):
    # Initialize variables
    n = len(game_state)
    k = 3
    x_count = 0
    o_count = 0
    x_row = [0] * n
    x_col = [0] * n
    x_diag = 0
    o_row = [0] * n
    o_col = [0] * n
    o_diag = 0

    # Loop through each cell in the board
    for i in range(n):
        for j in range(n):
            # If the cell is empty, continue to the next cell
            if game_state[i][j] == ".":
                continue

            # If the cell is an 'X', update the count and rows/columns/diagonals
            if game_state[i][j] == "X":
                x_count += 1
                x_row[i] += 1
                x_col[j] += 1
                if i == j:
                    x_diag += 1
                if i + j == n - 1:
                    x_diag += 1

            # If the cell is an 'O', update the count and rows/columns/diagonals
            if game_state[i][j] == "O":
                o_count += 1
                o_row[i] += 1
                o_col[j] += 1
                if i == j:
                    o_diag += 1
                if i + j == n - 1:
                    o_diag += 1

    # Check if X can win in one move
    for i in range(n):
        if x_row[i] + x_col[i] + x_diag == k and x_count + 1 == k:
            return "YES"
        if o_row[i] + o_col[i] + o_diag == k and o_count + 1 == k:
            return "YES"

    # Check if O can win in one move
    for i in range(n):
        if x_row[i] + x_col[i] + x_diag == k and x_count + 1 == k:
            return "YES"
        if o_row[i] + o_col[i] + o_diag == k and o_count + 1 == k:
            return "YES"

    # If no one can win in one move, return "NO"
    return "NO"

