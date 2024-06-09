
def is_box_large_enough(boxes, V):
    # Initialize the largest box and its volume to the first box
    largest_box = boxes[0]
    largest_volume = largest_box[0] * largest_box[1] * largest_box[2]

    # Iterate through the remaining boxes
    for i in range(1, len(boxes)):
        # Calculate the volume of the current box
        current_volume = boxes[i][0] * boxes[i][1] * boxes[i][2]

        # Check if the current box is larger than the largest box so far
        if current_volume > largest_volume:
            # If so, update the largest box and its volume
            largest_box = boxes[i]
            largest_volume = current_volume

    # Calculate the difference between the largest box's volume and V
    diff = largest_volume - V

    return diff

