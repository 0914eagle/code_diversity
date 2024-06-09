
def solve(n, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the sum of squares to 0
    sum_of_squares = 0
    # Loop through the array and calculate the sum of squares
    for i in range(n):
        sum_of_squares += a[i] ** 2
    # Return the sum of squares
    return sum_of_squares

