
def get_max_objects(objects, boxes, box_size):
    # Sort the objects by size in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed to 0
    num_packed = 0
    # Initialize the number of boxes used to 0
    num_boxes = 0
    # Initialize the remaining size of the current box to the box size
    remaining_size = box_size
    # Iterate through the objects
    for obj in objects:
        # Check if the object fits in the current box
        if obj <= remaining_size:
            # Increment the number of objects packed
            num_packed += 1
            # Decrement the remaining size of the current box
            remaining_size -= obj
        else:
            # Increment the number of boxes used
            num_boxes += 1
            # Check if the number of boxes used is less than the total number of boxes
            if num_boxes < boxes:
                # Reset the remaining size of the current box to the box size
                remaining_size = box_size
            else:
                # If all the boxes are used and the object does not fit, return the number of objects packed so far
                return num_packed
    # If all the objects are packed, return the total number of objects packed
    return num_packed + num_boxes * (box_size // objects[0])

