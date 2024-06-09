
def solve(n, V, boxes):
    # Initialize the largest box and its volume
    largest_box = None
    largest_volume = 0

    # Iterate through the boxes
    for box in boxes:
        # Calculate the volume of the current box
        volume = box[0] * box[1] * box[2]

        # If the current box is larger than the largest box, update the largest box and its volume
        if volume > largest_volume:
            largest_box = box
            largest_volume = volume

    # Calculate the difference between the largest box's volume and the target volume
    difference = largest_volume - V

    # Return the difference
    return difference

