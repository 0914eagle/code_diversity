
def get_max_objects(objects, boxes, box_size):
    # Sort the objects by size in non-decreasing order
    objects.sort()
    # Initialize the number of objects packed to 0
    num_packed = 0
    # Initialize the number of boxes used to 0
    num_boxes = 0
    # Initialize the size of the current box to 0
    current_box_size = 0
    # Iterate through the objects
    for obj in objects:
        # If the object fits in the current box
        if current_box_size + obj <= box_size:
            # Increment the number of objects packed
            num_packed += 1
            # Increment the size of the current box
            current_box_size += obj
        # If the object does not fit in the current box
        else:
            # If there are no more boxes available
            if num_boxes == boxes:
                # Return the number of objects packed so far
                return num_packed
            # Increment the number of boxes used
            num_boxes += 1
            # Reset the size of the current box
            current_box_size = obj
    # If all the objects have been packed
    return num_packed

