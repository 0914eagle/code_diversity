
def solve(n, s, l, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the number of pieces as 0
    pieces = 0
    # Initialize the start index of the current piece as 0
    start = 0
    # Loop through the array
    for i in range(n):
        # If the current number is greater than the maximum number in the current piece by more than s, start a new piece
        if a[i] - a[start] > s:
            pieces += 1
            start = i
        # If the current number is less than the minimum number in the current piece by more than s, start a new piece
        elif a[start] - a[i] > s:
            pieces += 1
            start = i
    # Add one more piece for the last part of the array
    pieces += 1
    # If the number of pieces is less than or equal to l, return the number of pieces
    if pieces <= l:
        return pieces
    # Otherwise, return -1
    else:
        return -1

