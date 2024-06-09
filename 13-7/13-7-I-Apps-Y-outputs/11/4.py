
def get_max_objects(n, m, k, a):
    # Sort the objects in descending order
    a.sort(reverse=True)
    # Initialize the number of objects packed
    count = 0
    # Initialize the number of boxes used
    boxes = 0
    # Initialize the current box size
    current_box_size = k
    for i in range(n):
        # Check if the current object fits in the current box
        if current_box_size >= a[i]:
            # Increment the number of objects packed
            count += 1
            # Decrement the current box size
            current_box_size -= a[i]
        else:
            # Increment the number of boxes used
            boxes += 1
            # Check if there are no more boxes available
            if boxes == m:
                # Return the number of objects packed
                return count
            # Reset the current box size to the maximum size
            current_box_size = k
    # Return the number of objects packed
    return count

