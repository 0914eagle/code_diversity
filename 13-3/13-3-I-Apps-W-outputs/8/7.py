
def is_possible(n, boxes):
    # Sort the boxes in non-decreasing order
    boxes.sort()

    # Initialize the sum of pieces for John and Sam as 0
    sum_john, sum_sam = 0, 0

    # Loop through the boxes
    for i in range(n):
        # If the current box contains an odd number of pieces, assign it to John
        if boxes[i] % 2 == 1:
            sum_john += boxes[i]
        # Otherwise, assign it to Sam
        else:
            sum_sam += boxes[i]

    # If the sums of pieces for John and Sam are equal, return YES
    if sum_john == sum_sam:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

