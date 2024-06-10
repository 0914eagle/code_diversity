
def min_cost_to_unlock_boxes(N, M, keys):
    keys.sort(key=lambda x: x[0] / x[1])  # Sort keys by cost per box

    total_cost = 0
    unlocked_boxes = set()
    for key in keys:
        cost, num_boxes = key
        for box in key[2:]:
            if box not in unlocked_boxes:
                total_cost += cost
                unlocked_boxes.add(box)
                if len(unlocked_boxes) == N:
                    return total_cost

    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    for _ in range(M):
        key_info = list(map(int, input().split()))
        keys.append(key_info)

    result = min_cost_to_unlock_boxes(N, M, keys)
    print(result)
