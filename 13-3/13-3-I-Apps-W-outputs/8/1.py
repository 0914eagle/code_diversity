
def is_possible(n, boxes):
    # Sort the boxes in non-decreasing order
    boxes.sort()
    # Initialize the sum of pieces for John and Sam as 0
    john_sum = 0
    sam_sum = 0
    # Loop through the boxes
    for box in boxes:
        # If the sum of pieces for John is less than the sum of pieces for Sam, give the box to John
        if john_sum < sam_sum:
            john_sum += box
        # Otherwise, give the box to Sam
        else:
            sam_sum += box
    # If the sum of pieces for John and Sam is the same, return YES
    if john_sum == sam_sum:
        return "YES"
    # Otherwise, return NO
    return "NO"

