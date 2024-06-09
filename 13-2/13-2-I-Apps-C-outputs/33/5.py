
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
    if (i, j, k, n) in memo:
        return memo[(i, j, k, n)]

    # Recursive case: solve the puzzle by moving the top disk from i to j, and the top disk from j to k
    cost1 = solve_small_y_puzzle_helper(t, n-1, i, k, j, cost+t[i-1][j-1], memo, min_cost)
    cost2 = solve_small_y_puzzle_helper(t, n-1, j, i, k, cost+t[j-1][i-1], memo, min_cost)

    # Update the minimum cost
    min_cost = min(min_cost, cost1, cost2)

    # Memoization: save the cost in the memoization dictionary
    memo[(i, j, k, n)] = min_cost

    # Return the minimum cost
    return min_cost

