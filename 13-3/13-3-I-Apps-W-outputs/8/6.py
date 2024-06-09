
def is_split_possible(num_boxes, boxes):
    # Sort the list of boxes in non-decreasing order
    boxes.sort()
    # Initialize the sum of pieces for John and Sam as 0
    sum_john, sum_sam = 0, 0
    # Loop through the boxes and assign them to John or Sam alternately
    for i in range(num_boxes):
        if i % 2 == 0:
            sum_john += boxes[i]
        else:
            sum_sam += boxes[i]
    # If the sum of pieces for John and Sam is equal, return YES
    if sum_john == sum_sam:
        return "YES"
    else:
        return "NO"

