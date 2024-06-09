
def is_box_big_enough(boxes, V):
    # Sort the boxes by volume in descending order
    sorted_boxes = sorted(boxes, key=lambda x: x[2], reverse=True)

    # Find the largest box by volume
    largest_box = sorted_boxes[0]

    # Calculate the difference between the largest box volume and V
    d = largest_box[2] - V

    return d

