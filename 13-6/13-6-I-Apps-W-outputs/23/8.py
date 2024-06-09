
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
        # If the current piece has a nut, calculate the number of ways to break the chocolate after it
        if arr[i] == 1:
            # Calculate the number of ways to break the chocolate before the current piece
            before = solve(i, arr[:i])

            # Calculate the number of ways to break the chocolate after the current piece
            after = solve(n - i - 1, arr[i + 1:])

            # Add the number of ways to break the chocolate before and after the current piece
            ways += before * after

    # Return the number of ways to break the chocolate
    return ways

