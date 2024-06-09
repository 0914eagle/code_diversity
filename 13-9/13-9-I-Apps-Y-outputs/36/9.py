
def get_largest_box_volume(n, V, boxes):
    # Initialize the largest box volume to 0
    largest_box_volume = 0

    # Iterate through the list of boxes
    for box in boxes:
        # Calculate the volume of the current box
        volume = box[0] * box[1] * box[2]

        # If the volume of the current box is greater than the largest box volume, update the largest box volume
        if volume > largest_box_volume:
            largest_box_volume = volume

    # Return the difference between the largest box volume and the target volume
    return largest_box_volume - V

