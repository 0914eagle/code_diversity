
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}

    # Initialize the minimum cost to infinity
    min_cost = float('inf')

    # Recursively solve the puzzle
    solve_small_y_puzzle_helper(t, n, 1, 2, 3, 0, memo, min_cost)

    # Return the minimum cost
    return min_cost

def solve_small_y_puzzle_helper(t, n, i, j, k, cost, memo, min_cost):
    # Base case: if the number of disks is 1, return the cost
    if n == 1:
        return cost

    # Memoization: if the state is already in the memoization dictionary, return the cost
    if (n, i, j, k) in memo:
        return memo[(n, i, j, k)]

    # Recursive case: solve the puzzle by moving the top disk from rod i to rod j
    cost1 = cost + t[i - 1][j - 1]
    cost2 = solve_small_y_puzzle_helper(t, n - 1, i, k, j, cost1, memo, min_cost)

    # Recursive case: solve the puzzle by moving the top disk from rod i to rod k
    cost3 = cost + t[i - 1][k - 1]
    cost4 = solve_small_y_puzzle_helper(t, n - 1, i, j, k, cost3, memo, min_cost)

    # Recursive case: solve the puzzle by moving the top disk from rod j to rod k
    cost5 = cost + t[j - 1][k - 1]
    cost6 = solve_small_y_puzzle_helper(t, n - 1, i, j, k, cost5, memo, min_cost)

    # Update the minimum cost
    min_cost = min(min_cost, cost2, cost4, cost6)

    # Memoization: save the cost in the memoization dictionary
    memo[(n, i, j, k)] = min_cost

    # Return the minimum cost
    return min_cost

