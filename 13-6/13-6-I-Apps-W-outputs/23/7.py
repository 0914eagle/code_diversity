
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
        # If the current piece has a nut, skip it
        if a[i] == 1:
            continue

        # Calculate the number of pieces with nuts to the left and right of the break point
        num_nuts_left = sum(a[:i])
        num_nuts_right = sum(a[i+1:])

        # If the number of nuts to the left and right of the break point is equal,
        # then the break point is valid
        if num_nuts_left == num_nuts_right:
            # Recursively call the function to find the number of ways to break the chocolate
            ways += solve(i, a[:i] + [1] + a[i+1:])

    return ways

