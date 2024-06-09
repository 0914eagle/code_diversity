
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

def main():
    # Read the number of boxes and the target volume from stdin
    n, V = map(int, input().split())

    # Read the dimensions of the boxes from stdin
    boxes = []
    for i in range(n):
        boxes.append(list(map(int, input().split())))

    # Call the get_largest_box function and print the result
    print(get_largest_box(boxes, V))

if __name__ == '__main__':
    main()

