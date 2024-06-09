
def is_largest_box_big_enough(boxes, V):
    largest_box = max(boxes, key=lambda x: x[0] * x[1] * x[2])
    return largest_box[0] * largest_box[1] * largest_box[2] - V

