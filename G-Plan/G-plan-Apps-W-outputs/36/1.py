
def can_cross_bridge(camels, bridge_parts):
    camels.sort()
    for part in bridge_parts:
        total_weight = 0
        for camel in camels:
            total_weight += camel
            if total_weight > part[1]:
                return -1
    return max(camels) - min(camels)

if __name__ == "__main__":
    N, M = map(int, input().split())
    camels = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]
    
    result = can_cross_bridge(camels, bridge_parts)
    print(result)
