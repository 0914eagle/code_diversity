
def solve(n, pieces):
    # Calculate the number of pieces with nuts
    num_nuts = sum(pieces)
    
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate over each possible break point
    for i in range(n - 1):
        # If the current piece has a nut, skip it
        if pieces[i] == 1:
            continue
        
        # Calculate the number of pieces with nuts on both sides of the break
        num_nuts_left = i
        num_nuts_right = num_nuts - i - 1
        
        # If the number of nuts on both sides is equal, recurse with the left and right subarrays
        if num_nuts_left == num_nuts_right:
            ways += solve(i, pieces[:i + 1]) * solve(n - i - 1, pieces[i + 1:])
    
    return ways

