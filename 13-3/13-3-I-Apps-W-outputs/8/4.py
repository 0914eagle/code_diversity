
def is_possible(n, boxes):
    # Sort the list of boxes in ascending order
    boxes.sort()
    # Initialize the sum of pieces for John and Sam as 0
    sum_john, sum_sam = 0, 0
    # Loop through the boxes and assign them to John or Sam alternatively
    for i in range(n):
        if i % 2 == 0:
            sum_john += boxes[i]
        else:
            sum_sam += boxes[i]
    # Check if the sum of pieces for John and Sam is the same
    if sum_john == sum_sam:
        return "YES"
    else:
        return "NO"

