
def get_largest_box_volume(boxes):
    return max(boxes, key=lambda x: x[0] * x[1] * x[2])

def get_largest_box_difference(boxes, V):
    largest_box = get_largest_box_volume(boxes)
    return largest_box[0] * largest_box[1] * largest_box[2] - V

def main():
    num_boxes, V = map(int, input().split())
    boxes = []
    for _ in range(num_boxes):
        boxes.append(list(map(int, input().split())))
    print(get_largest_box_difference(boxes, V))

if __name__ == '__main__':
    main()

