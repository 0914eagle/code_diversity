
def get_max_objects(objects, boxes, box_size):
    # Sort the objects in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed to 0
    num_packed = 0
    # Initialize the number of boxes used to 0
    num_boxes = 0
    # Loop through the objects
    for obj in objects:
        # If the current object fits in the current box
        if obj <= box_size:
            # Increment the number of objects packed
            num_packed += 1
            # Decrement the size of the current box
            box_size -= obj
        # If the current object does not fit in the current box
        else:
            # Increment the number of boxes used
            num_boxes += 1
            # Reset the size of the current box to its original size
            box_size = boxes[num_boxes-1]
    # Return the maximum number of objects that can be packed
    return num_packed

