
def can_cross_bridge(N, M, weights, parts):
    weights.sort()
    total_weight = 0

    for l, v in parts:
        for w in weights:
            if total_weight + w > v:
                return -1
            total_weight += w

    return max(weights) - min(weights)

if __name__ == "__main__":
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    parts = [list(map(int, input().split())) for _ in range(M)]

    result = can_cross_bridge(N, M, weights, parts)
    print(result)
