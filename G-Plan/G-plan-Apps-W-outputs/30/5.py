
def unlock_boxes(N, M, keys):
    keys.sort(key=lambda x: x[0] / x[1])  # Sort keys by cost per box
    total_cost = 0
    unlocked_boxes = set()
    
    for key in keys:
        cost, num_boxes = key
        for box in key[2:]:
            if box not in unlocked_boxes:
                total_cost += cost
                unlocked_boxes.add(box)
    
    return total_cost if len(unlocked_boxes) == N else -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = [list(map(int, input().split())) for _ in range(M)]
    print(unlock_boxes(N, M, keys))
