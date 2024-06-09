
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}
    
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Recursively solve the puzzle
    solve_small_y_puzzle_helper(t, n, 1, 2, 3, memo, min_cost)
    
    # Return the minimum cost
    return min_cost

def solve_small_y_puzzle_helper(t, n, i, j, k, memo, min_cost):
    # Base case: if there are no disks, return 0
    if n == 0:
        return 0
    
    # Base case: if the puzzle is already solved, return the minimum cost
    if i == k and j == k:
        return min_cost
    
    # If the puzzle is not in the memoization dictionary, calculate the cost and store it in the dictionary
    if (i, j, k) not in memo:
        # Calculate the cost of moving the top disk from rod i to rod j
        cost = t[i - 1][j - 1]
        
        # Recursively solve the puzzle by moving the top disk from rod i to rod k, and then moving the top disk from rod j to rod k
        cost += solve_small_y_puzzle_helper(t, n - 1, i, k, j, memo, min_cost)
        cost += solve_small_y_puzzle_helper(t, n - 1, j, k, i, memo, min_cost)
        
        # Store the cost in the memoization dictionary
        memo[(i, j, k)] = cost
    
    # If the puzzle is in the memoization dictionary, return the stored cost
    else:
        cost = memo[(i, j, k)]
    
    # Update the minimum cost if the current cost is less than the minimum cost
    if cost < min_cost:
        min_cost = cost
    
    # Return the minimum cost
    return min_cost

