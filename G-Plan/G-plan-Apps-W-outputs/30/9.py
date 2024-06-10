
def calculate_cost(keys, boxes):
    total_cost = 0
    unlocked_boxes = set()
    
    while len(unlocked_boxes) < len(boxes):
        min_cost = float('inf')
        key_to_buy = None
        
        for key in keys:
            cost_per_box = key[0] / len(set(key[1]) - unlocked_boxes)
            if cost_per_box < min_cost:
                min_cost = cost_per_box
                key_to_buy = key
        
        if key_to_buy is None:
            return -1
        
        total_cost += key_to_buy[0]
        unlocked_boxes.update(key_to_buy[1])
    
    return total_cost

if __name__ == "__main__":
    N, M = map(int, input().split())
    keys = []
    boxes = set(range(1, N+1))
    
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        keys.append((a, c))
    
    result = calculate_cost(keys, boxes)
    print(result)
