
def get_max_objects(objects, boxes, box_size):
    # Sort the objects in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed as 0
    num_packed = 0
    # Initialize the number of boxes used as 0
    num_boxes = 0
    # Initialize the remaining box size as the size of each box
    remaining_box_size = box_size
    # Iterate through the objects
    for obj in objects:
        # Check if the object fits in the current box
        if obj <= remaining_box_size:
            # Increment the number of objects packed
            num_packed += 1
            # Decrement the remaining box size by the object size
            remaining_box_size -= obj
        else:
            # If the object does not fit, start a new box
            num_boxes += 1
            # Reset the remaining box size to the size of each box
            remaining_box_size = box_size
    # Return the maximum number of objects packed
    return num_packed + num_boxes * (box_size // objects[0])

