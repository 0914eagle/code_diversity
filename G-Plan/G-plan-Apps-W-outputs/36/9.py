
def can_cross_bridge(camels, bridge_parts):
    camels.sort()
    total_weight = 0

    for l, v in bridge_parts:
        for camel in camels:
            if total_weight + camel > v:
                return -1
            total_weight += camel

    return sum(camels[:-1]) - camels[0]

if __name__ == "__main__":
    N, M = map(int, input().split())
    camels = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]

    result = can_cross_bridge(camels, bridge_parts)
    print(result)
