
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}

    # Initialize the minimum cost to solve the puzzle
    min_cost = float('inf')

    # Recursively solve the puzzle
    solve_small_y_puzzle_helper(t, n, 1, 2, 3, 0, memo)

    # Return the minimum cost to solve the puzzle
    return min_cost

def solve_small_y_puzzle_helper(t, n, i, j, k, cost, memo):
    # Base case: if the number of disks is 1, return the cost of moving the disk from i to j
    if n == 1:
        return t[i - 1][j - 1]

    # Memoization: if the state has already been visited, return the memoized value
    if (i, j, k, n) in memo:
        return memo[(i, j, k, n)]

    # Recursive call: solve the puzzle by moving the top disk from i to j, and the top disk from j to k, and the top disk from i to k
    cost1 = t[i - 1][j - 1] + solve_small_y_puzzle_helper(t, n - 1, j, k, i, cost + t[i - 1][j - 1], memo)
    cost2 = t[j - 1][k - 1] + solve_small_y_puzzle_helper(t, n - 1, i, j, k, cost + t[j - 1][k - 1], memo)
    cost3 = t[i - 1][k - 1] + solve_small_y_puzzle_helper(t, n - 1, j, k, i, cost + t[i - 1][k - 1], memo)

    # Update the minimum cost
    min_cost = min(cost1, cost2, cost3)

    # Memoize the state and return the minimum cost
    memo[(i, j, k, n)] = min_cost
    return min_cost

