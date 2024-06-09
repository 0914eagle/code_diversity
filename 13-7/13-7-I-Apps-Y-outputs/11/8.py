
def get_max_objects(objects, boxes, box_size):
    # Sort the objects by size in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed to 0
    num_packed = 0
    # Initialize the number of boxes used to 0
    num_boxes = 0
    # Initialize the current box size to 0
    current_box_size = 0
    # Iterate through the objects
    for obj in objects:
        # If the current box size plus the current object size is less than or equal to the box size
        if current_box_size + obj <= box_size:
            # Increment the number of objects packed
            num_packed += 1
            # Increment the current box size by the current object size
            current_box_size += obj
        # If the current box size is 0 and the number of boxes used is less than the number of boxes available
        elif current_box_size == 0 and num_boxes < boxes:
            # Increment the number of boxes used
            num_boxes += 1
            # Set the current box size to the current object size
            current_box_size = obj
        # If the current box size is not 0 and the number of boxes used is equal to the number of boxes available
        elif current_box_size != 0 and num_boxes == boxes:
            # Return the number of objects packed
            return num_packed
        # If the current box size is not 0 and the number of boxes used is less than the number of boxes available
        elif current_box_size != 0 and num_boxes < boxes:
            # Increment the number of boxes used
            num_boxes += 1
            # Set the current box size to the current object size
            current_box_size = obj
    # Return the number of objects packed
    return num_packed

