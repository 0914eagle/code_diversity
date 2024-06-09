
def solve(n, a):
    # Initialize variables
    seconds = 0
    k = 1
    divisible_boxes = []

    # Loop through each box
    for i in range(n):
        # If the current box is not divisible by k, find the next divisor of a[i]
        while a[i] % k != 0:
            k += 1

        # If k is greater than the number of chocolates in the current box, return -1
        if k > a[i]:
            return -1

        # If the current box is divisible by k, add it to the list of divisible boxes
        if a[i] % k == 0:
            divisible_boxes.append(i)

    # If all boxes are divisible by k, return the number of seconds
    if len(divisible_boxes) == n:
        return seconds

    # If not all boxes are divisible by k, find the box with the smallest number of chocolates
    smallest_box = 0
    for i in range(n):
        if a[i] < a[smallest_box]:
            smallest_box = i

    # Move a piece of chocolate from the smallest box to the next box
    a[smallest_box] -= 1
    a[smallest_box + 1] += 1
    seconds += 1

    # Recursively call the function to solve the updated problem
    return solve(n, a)

