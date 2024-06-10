
def calculate_cost(keys, prices, boxes):
    total_cost = 0
    unlocked_boxes = set()
    
    while len(unlocked_boxes) < len(boxes):
        min_cost = float('inf')
        selected_key = -1
        
        for i, key in enumerate(keys):
            cost_per_box = prices[i] / len(set(boxes[key]) - unlocked_boxes)
            if cost_per_box < min_cost:
                min_cost = cost_per_box
                selected_key = i
        
        if selected_key == -1:
            return -1
        
        total_cost += prices[selected_key]
        unlocked_boxes.update(boxes[keys[selected_key]])
    
    return total_cost

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    prices = []
    boxes = {}
    
    for _ in range(M):
        a, b = map(int, input().split())
        keys.append(list(map(int, input().split())))
        prices.append(a)
        for box in keys[-1]:
            if box not in boxes:
                boxes[box] = []
            boxes[box].append(keys[-1])
    
    result = calculate_cost(range(M), prices, boxes)
    print(result)
