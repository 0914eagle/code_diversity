
def solve(n, a):
    # Calculate the number of pieces with nuts
    num_nuts = sum(a)
    
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate over each possible break point
    for i in range(n - 1):
        # Calculate the number of pieces with nuts on each side of the break
        num_nuts_left = sum(a[:i + 1])
        num_nuts_right = num_nuts - num_nuts_left
        
        # Check if the number of nuts on each side is equal to the total number of nuts
        if num_nuts_left == num_nuts_right:
            # Recursively call the function to break the chocolate into two parts
            ways += solve(i + 1, a[i + 1:]) * solve(n - i - 1, a[:i + 1])
    
    return ways

