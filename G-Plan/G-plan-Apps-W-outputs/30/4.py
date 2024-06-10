
def unlock_boxes(N, M, keys):
    boxes = [0] * (N + 1)
    total_cost = 0

    for _ in range(N):
        min_cost = float('inf')
        selected_key = -1

        for i, (price, num_boxes, box_numbers) in enumerate(keys):
            cost_per_box = price / num_boxes
            if cost_per_box < min_cost:
                min_cost = cost_per_box
                selected_key = i

        if selected_key == -1:
            print(-1)
            return

        for box_num in keys[selected_key][2]:
            boxes[box_num] = 1

        total_cost += keys[selected_key][0]

    print(total_cost)


if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        keys.append((a, b, c))

    unlock_boxes(N, M, keys)
