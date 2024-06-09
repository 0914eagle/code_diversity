
def is_split_possible(number_of_boxes, boxes):
    # Sort the list of boxes in ascending order
    boxes.sort()
    # Initialize the sum of pieces of chocolate for John and Sam as 0
    sum_john, sum_sam = 0, 0
    # Initialize the number of boxes used as 0
    num_boxes_used = 0
    # Loop through the list of boxes
    for box in boxes:
        # If the sum of pieces of chocolate for John is less than the sum of pieces of chocolate for Sam, give the current box to John
        if sum_john < sum_sam:
            sum_john += box
            num_boxes_used += 1
        # Otherwise, give the current box to Sam
        else:
            sum_sam += box
            num_boxes_used += 1
    # If the sum of pieces of chocolate for John and Sam is the same, return YES
    if sum_john == sum_sam:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

