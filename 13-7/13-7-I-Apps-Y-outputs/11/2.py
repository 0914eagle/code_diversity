
def get_max_objects(n, m, k, a):
    # Sort the objects in non-decreasing order
    a.sort()
    # Initialize the number of objects that can be packed to 0
    max_objects = 0
    # Loop through each object and try to pack it
    for i in range(n):
        # Check if the current object fits in any of the boxes
        for j in range(m):
            if a[i] <= k:
                # If the object fits in the current box, add it to the box
                max_objects += 1
                break
        # If the object does not fit in any box, throw it out
        else:
            max_objects += 1
            break
    return max_objects

