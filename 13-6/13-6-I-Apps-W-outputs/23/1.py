
def solve(n, arr):
    # Calculate the number of pieces with nuts
    num_nuts = sum(arr)
    # Base case: if there is only one piece, return 1
    if n == 1:
        return 1
    # Initialize the number of ways to break the chocolate to 0
    ways = 0
    # Loop through each piece
    for i in range(n):
        # If the current piece has a nut
        if arr[i] == 1:
            # Calculate the number of ways to break the chocolate starting from the current piece
            ways += solve(n - i - 1, arr[i + 1:])
    # Return the number of ways to break the chocolate
    return ways

