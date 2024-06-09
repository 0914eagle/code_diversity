
def solve(n, V, boxes):
    # Sort the boxes by volume in descending order
    boxes = sorted(boxes, key=lambda x: x[0] * x[1] * x[2], reverse=True)

    # Find the largest box by volume
    largest_box = boxes[0]

    # Calculate the difference between the largest box volume and V
    d = largest_box[0] * largest_box[1] * largest_box[2] - V

    return d

