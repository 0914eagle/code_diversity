
def min_seconds(n, a):
    # Initialize variables
    seconds = 0
    k = 1
    divisible_by_k = [False] * n

    # Iterate through the boxes
    for i in range(n):
        # If the current box is not divisible by k, find the next available divisor
        while a[i] % k != 0:
            k += 1

        # If we have reached a prime number, return -1
        if k == a[i]:
            return -1

        # Mark the current box as divisible by k
        divisible_by_k[i] = True
        seconds += 1

        # If all boxes are divisible by k, return the number of seconds
        if all(divisible_by_k):
            return seconds

    # If we reach this point, it means that we have not been able to make all boxes divisible by k
    return -1

