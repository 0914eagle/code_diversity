
def get_max_objects(objects, boxes, box_size):
    # Sort the objects by size in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed as 0
    num_packed = 0
    # Initialize the number of boxes used as 0
    num_boxes = 0
    # Initialize the current box size as 0
    current_box_size = 0
    # Iterate through the objects
    for obj in objects:
        # If the current object fits in the current box
        if current_box_size + obj <= box_size:
            # Increment the number of objects packed
            num_packed += 1
            # Increment the current box size by the object size
            current_box_size += obj
        # If the current object does not fit in the current box
        else:
            # Increment the number of boxes used
            num_boxes += 1
            # Reset the current box size to 0
            current_box_size = 0
            # If the number of boxes used is equal to the number of boxes available
            if num_boxes == boxes:
                # Break out of the loop
                break
    # Return the maximum number of objects packed
    return num_packed

