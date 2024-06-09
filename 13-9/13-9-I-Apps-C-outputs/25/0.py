
def find_min_seconds(n, a):
    # Initialize variables
    seconds = 0
    k = 1
    is_happy = False

    # Loop through each box and its chocolate pieces
    for i in range(n):
        # If the current box is not empty and the number of pieces is not divisible by k, find the next divisor of the number of pieces
        if a[i] > 0 and a[i] % k != 0:
            while a[i] % k != 0:
                k += 1

        # If the current box is not empty and the number of pieces is divisible by k, move the pieces to the next box
        if a[i] > 0 and a[i] % k == 0:
            seconds += 1
            a[i] = 0
            if i < n - 1:
                a[i+1] += a[i]
            else:
                a[1] += a[i]

    # If at least one box is not empty, continue the loop
    if any(a):
        seconds += find_min_seconds(n, a)

    return seconds

