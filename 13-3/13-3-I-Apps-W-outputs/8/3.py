
def is_split_possible(number_of_boxes, boxes_of_chocolate):
    # Sort the list of boxes of chocolate in descending order
    sorted_boxes = sorted(boxes_of_chocolate, reverse=True)
    # Initialize variables to keep track of the number of pieces of chocolate for John and Sam
    john_pieces = 0
    sam_pieces = 0
    # Loop through the sorted list of boxes of chocolate
    for box in sorted_boxes:
        # If the number of pieces of chocolate in the current box is odd, assign it to John
        if box % 2 == 1:
            john_pieces += box
        # Otherwise, assign it to Sam
        else:
            sam_pieces += box
    # If the number of pieces of chocolate for John and Sam is the same, return YES
    if john_pieces == sam_pieces:
        return "YES"
    # Otherwise, return NO
    else:
        return "NO"

