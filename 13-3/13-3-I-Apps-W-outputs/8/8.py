
def is_possible(n, boxes):
    # Sort the boxes in non-decreasing order
    boxes.sort()

    # Initialize the sum of pieces for John and Sam as 0
    john_sum = 0
    sam_sum = 0

    # Loop through the boxes
    for i in range(n):
        # If the current box has an odd number of pieces, assign it to John
        if boxes[i] % 2 == 1:
            john_sum += boxes[i]
        # Otherwise, assign it to Sam
        else:
            sam_sum += boxes[i]

    # If the sums are equal, return YES
    if john_sum == sam_sum:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

