
def get_max_objects(n, m, k, a):
    # Initialize the number of objects that can be packed
    max_objects = 0
    # Initialize the number of boxes that are still empty
    empty_boxes = m
    # Initialize the current box number
    current_box = 1
    # Initialize the current box size
    current_box_size = k
    # Initialize the number of objects that are left to pack
    objects_left = n
    # Sort the objects in descending order
    a.sort(reverse=True)
    # Loop through the objects and try to pack them into the boxes
    for i in range(n):
        # Check if the current object fits in the current box
        if current_box_size >= a[i]:
            # If it fits, pack it and decrease the current box size
            current_box_size -= a[i]
            # Decrease the number of objects that are left to pack
            objects_left -= 1
        else:
            # If it doesn't fit, move to the next box
            current_box += 1
            # Check if there are any empty boxes left
            if empty_boxes > 0:
                # If there are, move to the next box and make it the current box
                current_box_size = k
                empty_boxes -= 1
            else:
                # If there are no empty boxes left, break the loop
                break
        # Update the maximum number of objects that can be packed
        max_objects = max(max_objects, n - objects_left)
    # Return the maximum number of objects that can be packed
    return max_objects

