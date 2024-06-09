
def is_split_possible(num_boxes, boxes):
    # Sort the list of boxes in ascending order
    boxes.sort()
    # Initialize the sum of pieces of chocolate for John and Sam as 0
    sum_john, sum_sam = 0, 0
    # Iterate through the list of boxes
    for i in range(num_boxes):
        # If the current box contains an odd number of pieces, assign it to John
        if boxes[i] % 2 == 1:
            sum_john += boxes[i]
        # Otherwise, assign it to Sam
        else:
            sum_sam += boxes[i]
    # If the sum of pieces of chocolate for John and Sam is equal, return YES
    if sum_john == sum_sam:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

