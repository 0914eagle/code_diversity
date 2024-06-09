
def solve(n, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the sum of squares
    sum_of_squares = 0
    # Loop through the array and calculate the sum of squares
    for i in range(n):
        sum_of_squares += a[i] * a[i]
    return sum_of_squares

