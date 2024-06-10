
def unlock_boxes(N, M, keys):
    keys.sort(key=lambda x: x[0] / x[1])  # Sort keys by cost per box
    total_cost = 0
    unlocked_boxes = set()
    
    for key_price, num_boxes, boxes in keys:
        cost_per_box = key_price / num_boxes
        for box in boxes:
            if box not in unlocked_boxes:
                total_cost += key_price
                unlocked_boxes.add(box)
    
    return total_cost if len(unlocked_boxes) == N else -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        keys.append((a, b, c))
    
    print(unlock_boxes(N, M, keys))
