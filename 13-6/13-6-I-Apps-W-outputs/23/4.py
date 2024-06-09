
def solve(n, pieces):
    # Calculate the number of pieces with nuts
    num_nuts = sum(pieces)
    
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate over each piece
    for i in range(n):
        # If the current piece has a nut, remove it and calculate the number of ways to break the remaining pieces
        if pieces[i] == 1:
            ways += solve(n-1, pieces[:i] + pieces[i+1:])
    
    # Return the number of ways to break the chocolate
    return ways

