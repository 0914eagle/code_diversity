
def is_split_possible(number_of_boxes, boxes):
    # Sort the list of boxes in ascending order
    boxes.sort()
    # Initialize the sum of pieces of chocolate for John and Sam as 0
    sum_john, sum_sam = 0, 0
    # Initialize the number of boxes used as 0
    num_boxes_used = 0
    # Loop through the boxes
    for box in boxes:
        # If the sum of pieces of chocolate for John and Sam is equal, break the loop
        if sum_john == sum_sam:
            break
        # If the sum of pieces of chocolate for John and Sam is not equal, add the pieces of chocolate in the current box to the sum
        if sum_john < sum_sam:
            sum_john += box
            num_boxes_used += 1
        else:
            sum_sam += box
            num_boxes_used += 1
    # If all the boxes are used and the sum of pieces of chocolate for John and Sam is equal, return YES
    if num_boxes_used == number_of_boxes and sum_john == sum_sam:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

