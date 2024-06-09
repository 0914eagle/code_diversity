
def get_max_objects(n, m, k, a):
    # Initialize the number of objects that can be packed
    max_objects = 0
    # Initialize the number of empty boxes
    empty_boxes = m
    # Initialize the current box size
    current_box_size = k
    # Initialize the current number of objects packed
    current_objects = 0

    # Sort the objects in descending order
    a.sort(reverse=True)

    # Iterate through the objects
    for i in range(n):
        # Check if the current object fits in the current box
        if current_box_size >= a[i]:
            # If it fits, pack it and decrease the current box size
            current_box_size -= a[i]
            current_objects += 1
        else:
            # If it doesn't fit, move to the next box
            empty_boxes -= 1
            if empty_boxes == 0:
                # If there are no more empty boxes, return the current number of objects packed
                return current_objects
            current_box_size = k

    # If all the objects were packed, return the current number of objects packed
    return current_objects


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
print(get_max_objects(n, m, k, a))

