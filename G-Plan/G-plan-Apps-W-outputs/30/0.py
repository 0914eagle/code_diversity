
def unlock_boxes(N, M, keys):
    boxes = [False] * N
    total_cost = 0

    while not all(boxes):
        min_cost = float('inf')
        key_to_use = None

        for key in keys:
            cost, num_boxes, box_nums = key
            cost_per_box = cost / num_boxes

            if cost_per_box < min_cost:
                min_cost = cost_per_box
                key_to_use = key

        if key_to_use is None:
            print(-1)
            return

        for box_num in key_to_use[2]:
            boxes[box_num - 1] = True

        total_cost += key_to_use[0]

    print(total_cost)


if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []

    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        keys.append((a, b, c))

    unlock_boxes(N, M, keys)
