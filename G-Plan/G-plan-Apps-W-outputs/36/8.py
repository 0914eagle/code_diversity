k_bridge_crossing_possible(camels, bridge_parts):
    camels.sort()
    total_weight = 0
    for part in bridge_parts:
        for camel in camels:
            if total_weight + camel > part[1]:
                return -1
            total_weight += camel
    return total_weight

def find_minimum_distance(camels, bridge_parts):
    min_distance = 0
    max_distance = sum(camels)
    while min_distance < max_distance:
        mid_distance = (min_distance + max_distance) // 2
        if check_bridge_crossing_possible(camels, bridge_parts, mid_distance) != -1:
            max_distance = mid_distance
        else:
            min_distance = mid_distance + 1
    return min_distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    camels = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_minimum_distance(camels, bridge_parts)
    print(result)
