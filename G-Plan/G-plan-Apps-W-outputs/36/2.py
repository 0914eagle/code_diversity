cross_bridge(camels, bridge_parts):
    camels.sort()
    total_weight = 0

    for length, capacity in bridge_parts:
        for camel in camels:
            if total_weight + camel > capacity:
                return -1
            total_weight += camel

    return total_weight

def min_distance_between_camels(camels, bridge_parts):
    min_distance = float('inf')
    for i in range(len(camels) - 1):
        distance = camels[i + 1] - camels[i]
        min_distance = min(min_distance, distance)

    return min_distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    camels = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]

    result = can_cross_bridge(camels, bridge_parts)
    if result == -1:
        print(-1)
    else:
        print(min_distance_between_camels(camels, bridge_parts)