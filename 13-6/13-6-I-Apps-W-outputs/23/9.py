
def solve(n, arr):
    # Calculate the number of pieces with nuts
    num_nuts = sum(arr)

    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1

    # Initialize the number of ways to break the chocolate
    ways = 0

    # Iterate over each piece
    for i in range(n):
        # If the current piece has a nut, calculate the number of ways to break the chocolate after breaking the current piece
        if arr[i] == 1:
            # Calculate the number of pieces with nuts after breaking the current piece
            num_nuts_after = num_nuts - 1

            # Calculate the number of ways to break the chocolate after breaking the current piece
            ways_after = solve(n - i - 1, arr[i + 1:])

            # Add the number of ways to break the chocolate after breaking the current piece to the total number of ways
            ways += ways_after

    # Return the total number of ways to break the chocolate
    return ways

