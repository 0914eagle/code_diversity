
def get_max_objects(objects, boxes, box_size):
    # Sort the objects by size in descending order
    objects.sort(reverse=True)
    # Initialize the number of objects packed to 0
    num_packed = 0
    # Loop through the objects and try to pack them into the boxes
    for obj in objects:
        # Check if the object fits in any of the boxes
        for box in range(boxes):
            if box_size[box] >= obj:
                # If the object fits, pack it into the box and decrease the box size
                box_size[box] -= obj
                num_packed += 1
                break
        else:
            # If the object doesn't fit in any of the boxes, return the current number of packed objects
            return num_packed
    # If all the objects are packed, return the total number of packed objects
    return num_packed

