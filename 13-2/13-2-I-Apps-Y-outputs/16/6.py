
def get_largest_box(boxes, V):
    # Initialize the largest box and its volume to the first box
    largest_box = boxes[0]
    largest_volume = get_volume(largest_box)

    # Iterate through the remaining boxes
    for i in range(1, len(boxes)):
        # Calculate the volume of the current box
        current_volume = get_volume(boxes[i])

        # If the current box has a larger volume than the largest box, update the largest box and its volume
        if current_volume > largest_volume:
            largest_box = boxes[i]
            largest_volume = current_volume

    # Return the difference between the largest box's volume and the target volume
    return largest_volume - V

def get_volume(box):
    # Unpack the dimensions of the box
    l, w, h = box

    # Calculate the volume of the box
    return l * w * h

if __name__ == '__main__':
    # Read the input
    n, V = map(int, input().split())
    boxes = []
    for _ in range(n):
        boxes.append(list(map(int, input().split())))

    # Call the function to get the largest box and its volume
    largest_box = get_largest_box(boxes, V)

    # Print the result
    print(largest_box)

