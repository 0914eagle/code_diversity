
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}

    # Initialize the minimum cost to solve the puzzle
    min_cost = float('inf')

    # Recursively solve the puzzle
    solve_small_y_puzzle_helper(t, n, 1, 2, 3, memo, min_cost)

    # Return the minimum cost to solve the puzzle
    return min_cost

def solve_small_y_puzzle_helper(t, n, i, j, k, memo, min_cost):
    # Base case: if there are no disks left to move, return 0
    if n == 0:
        return 0

    # Base case: if the current configuration has already been visited, return the memoized value
    if (n, i, j, k) in memo:
        return memo[(n, i, j, k)]

    # Recursive case: move the top disk from rod i to rod j
    cost1 = t[i - 1][j - 1] + solve_small_y_puzzle_helper(t, n - 1, i, k, j, memo, min_cost)

    # Recursive case: move the top disk from rod i to rod k
    cost2 = t[i - 1][k - 1] + solve_small_y_puzzle_helper(t, n - 1, i, j, k, memo, min_cost)

    # Recursive case: move the top disk from rod j to rod k
    cost3 = t[j - 1][k - 1] + solve_small_y_puzzle_helper(t, n - 1, i, j, k, memo, min_cost)

    # Memoize the current configuration and return the minimum cost
    memo[(n, i, j, k)] = min(cost1, cost2, cost3)
    return memo[(n, i, j, k)]

