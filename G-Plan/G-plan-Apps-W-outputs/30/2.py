
def unlock_boxes(N, M, keys):
    keys.sort(key=lambda x: x[0] / x[1])  # Sort keys by cost per box unlocked
    total_cost = 0
    unlocked_boxes = set()
    
    for price, num_boxes, boxes in keys:
        for box in boxes:
            if box not in unlocked_boxes:
                total_cost += price
                unlocked_boxes.add(box)
        
        if len(unlocked_boxes) == N:
            return total_cost
    
    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        keys.append((a, b, c))
    
    result = unlock_boxes(N, M, keys)
    print(result)
