
def max_box_volume(n, V, boxes):
    # Find the largest box by volume
    largest_box = max(boxes, key=lambda x: x[0] * x[1] * x[2])

    # Calculate the difference between the largest box volume and the target volume
    diff = largest_box[0] * largest_box[1] * largest_box[2] - V

    return diff

