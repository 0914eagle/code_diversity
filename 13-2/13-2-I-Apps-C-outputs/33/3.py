
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}

    # Initialize the minimum cost to infinity
    min_cost = float('inf')

    # Recursively solve the puzzle
    solve_small_y_puzzle_recursive(t, n, 1, 2, 3, memo, min_cost)

    # Return the minimum cost
    return min_cost

def solve_small_y_puzzle_recursive(t, n, i, j, k, memo, min_cost):
    # Base case: if there are no disks, return 0
    if n == 0:
        return 0

    # If the current state is already in the memoization dictionary, return the stored value
    if (n, i, j, k) in memo:
        return memo[(n, i, j, k)]

    # Initialize the minimum cost for the current state
    min_cost_current_state = float('inf')

    # Try moving the top disk from rod i to rod j
    cost_move_i_to_j = t[i - 1][j - 1]
    cost_move_i_to_j += solve_small_y_puzzle_recursive(t, n - 1, i, k, j, memo, min_cost)

    # Try moving the top disk from rod i to rod k
    cost_move_i_to_k = t[i - 1][k - 1]
    cost_move_i_to_k += solve_small_y_puzzle_recursive(t, n - 1, i, j, k, memo, min_cost)

    # Try moving the top disk from rod j to rod k
    cost_move_j_to_k = t[j - 1][k - 1]
    cost_move_j_to_k += solve_small_y_puzzle_recursive(t, n - 1, j, i, k, memo, min_cost)

    # Update the minimum cost for the current state
    min_cost_current_state = min(cost_move_i_to_j, cost_move_i_to_k, cost_move_j_to_k)

    # Store the minimum cost in the memoization dictionary
    memo[(n, i, j, k)] = min_cost_current_state

    # Update the global minimum cost
    min_cost = min(min_cost, min_cost_current_state)

    # Return the minimum cost for the current state
    return min_cost_current_state

