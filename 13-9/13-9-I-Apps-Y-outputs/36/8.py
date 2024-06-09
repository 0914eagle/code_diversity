
def is_box_big_enough(boxes, V):
    # Sort the boxes by volume in descending order
    sorted_boxes = sorted(boxes, key=lambda x: x[2], reverse=True)

    # Initialize the largest box and its volume
    largest_box = sorted_boxes[0]
    largest_volume = largest_box[2]

    # Calculate the difference between the largest box volume and V
    difference = largest_volume - V

    return difference

