
def get_max_objects(n, m, k, a):
    # Initialize the number of objects that can be packed
    max_objects = 0
    # Initialize the number of boxes that are still empty
    empty_boxes = m
    # Initialize the current box size
    current_box_size = k
    # Initialize the current number of objects that have been packed
    current_objects = 0

    # Sort the objects in descending order
    a.sort(reverse=True)

    # Iterate through the objects
    for i in range(n):
        # Check if the current object fits in the current box
        if current_box_size >= a[i]:
            # If it fits, pack it in the current box
            current_box_size -= a[i]
            current_objects += 1
        else:
            # If it doesn't fit, move to the next box
            empty_boxes -= 1
            current_box_size = k
            current_objects = 0

        # Update the maximum number of objects that can be packed
        max_objects = max(max_objects, current_objects)

        # If there are no more empty boxes and not all objects have been packed, return -1
        if empty_boxes == 0 and current_objects < n:
            return -1

    # Return the maximum number of objects that can be packed
    return max_objects

