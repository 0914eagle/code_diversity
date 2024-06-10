
def can_cross_bridge(camels, bridge_parts):
    camels.sort()
    total_weight = 0

    for length, capacity in bridge_parts:
        for weight in camels:
            if total_weight + weight > capacity:
                return -1
            total_weight += weight

    return sum(camels[:-1]) - sum(camels[1:])

if __name__ == "__main__":
    N, M = map(int, input().split())
    camels = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]

    result = can_cross_bridge(camels, bridge_parts)
    print(result)
