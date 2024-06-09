
def get_max_objects(n, m, k, a):
    # Sort the objects in descending order
    a.sort(reverse=True)
    # Initialize the number of objects packed
    num_packed = 0
    # Initialize the number of boxes used
    num_boxes = 0
    # Initialize the size of the current box
    curr_box_size = 0
    # Iterate through the objects
    for i in range(n):
        # Check if the current object fits in the current box
        if curr_box_size + a[i] <= k:
            # If it fits, add it to the current box
            curr_box_size += a[i]
            num_packed += 1
        # If the current object does not fit in the current box
        else:
            # If we have used all the boxes, return the number of objects packed
            if num_boxes == m:
                return num_packed
            # Otherwise, start a new box
            num_boxes += 1
            curr_box_size = a[i]
    # If we have packed all the objects, return the number of objects packed
    return num_packed

