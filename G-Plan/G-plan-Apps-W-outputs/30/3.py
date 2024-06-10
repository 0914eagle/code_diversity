
def find_min_cost(N, M, keys):
    keys.sort(key=lambda x: x[0] / x[1])  # Sort keys by cost per box
    boxes_unlocked = set()
    total_cost = 0

    for key_cost, num_boxes, box_numbers in keys:
        cost_per_box = key_cost / num_boxes
        boxes_to_unlock = set(box_numbers) - boxes_unlocked
        if not boxes_to_unlock:
            continue

        total_cost += key_cost
        boxes_unlocked.update(boxes_to_unlock)

        if len(boxes_unlocked) == N:
            return total_cost

    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    for _ in range(M):
        key_info = list(map(int, input().split()))
        box_numbers = list(map(int, input().split()))
        keys.append((key_info[0], key_info[1], box_numbers))

    result = find_min_cost(N, M, keys)
    print(result)
