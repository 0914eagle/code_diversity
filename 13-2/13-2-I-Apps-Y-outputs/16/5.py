
def get_largest_box(boxes, V):
    largest_box = None
    for box in boxes:
        if largest_box is None or box[0] * box[1] * box[2] > largest_box[0] * largest_box[1] * largest_box[2]:
            largest_box = box
    return largest_box[0] * largest_box[1] * largest_box[2] - V

def main():
    num_boxes, V = map(int, input().split())
    boxes = []
    for _ in range(num_boxes):
        boxes.append(list(map(int, input().split())))
    print(get_largest_box(boxes, V))

if __name__ == '__main__':
    main()

