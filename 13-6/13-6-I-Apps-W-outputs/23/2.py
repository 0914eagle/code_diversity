
def break_chocolate(n, pieces):
    # Calculate the number of pieces with nuts
    num_nuts = sum(pieces)
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    # Initialize the number of ways to break the chocolate
    ways = 0
    # Iterate over each piece
    for i in range(n):
        # If the current piece has a nut, try breaking the chocolate in two ways
        if pieces[i] == 1:
            # Recursively call the function with the left and right parts of the chocolate
            ways += break_chocolate(i, pieces[:i] + pieces[i+1:])
            # If the current piece does not have a nut, try breaking the chocolate in one way
        else:
            ways += break_chocolate(i, pieces[:i] + pieces[i+1:])
    return ways

