cross_bridge(N, M, weights, bridge_parts):
    weights.sort()
    total_weight = 0

    for l, v in bridge_parts:
        for w in weights:
            if total_weight + w > v:
                return -1
            total_weight += w

    return weights[-1] - weights[0]

if __name__ == "__main__":
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    bridge_parts = [list(map(int, input().split())) for _ in range(M)]

    result = can_cross_bridge(N, M, weights, bridge_parts)
    print(result