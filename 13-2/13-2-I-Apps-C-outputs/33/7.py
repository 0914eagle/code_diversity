
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}
    
    # Calculate the minimum cost of solving the puzzle
    cost = solve_small_y_puzzle_helper(t, n, 1, 3, memo)
    
    # Return the minimum cost
    return cost

def solve_small_y_puzzle_helper(t, n, i, j, memo):
    # Base case: if there is only one disk, return the cost of moving it
    if n == 1:
        return t[i][j]
    
    # Memoization: if the state has already been calculated, return the result
    if (n, i, j) in memo:
        return memo[(n, i, j)]
    
    # Initialize the minimum cost to infinity
    cost = float('inf')
    
    # Consider all possible moves
    for k in range(1, 4):
        # If k is not the current rod and k is not the destination rod, consider moving the top disk from the current rod to the k rod
        if k != i and k != j:
            # Calculate the cost of moving the top disk from the current rod to the k rod
            cost1 = t[i][k] + solve_small_y_puzzle_helper(t, n-1, k, j, memo)
            # If the cost is less than the current minimum cost, update the minimum cost
            if cost1 < cost:
                cost = cost1
        # If k is the destination rod, consider moving the top disk from the current rod to the destination rod
        elif k == j:
            # Calculate the cost of moving the top disk from the current rod to the destination rod
            cost2 = t[i][k] + solve_small_y_puzzle_helper(t, n-1, i, j, memo)
            # If the cost is less than the current minimum cost, update the minimum cost
            if cost2 < cost:
                cost = cost2
    
    # Memoize the result for the current state
    memo[(n, i, j)] = cost
    
    # Return the minimum cost
    return cost

