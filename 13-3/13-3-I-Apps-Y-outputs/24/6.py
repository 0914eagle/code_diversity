
def get_flavor(N, L):
    apples = [int(input()) for _ in range(N)]
    total_flavor = sum(apples)
    min_diff = total_flavor
    for i in range(N):
        flavor = total_flavor - apples[i]
        diff = abs(flavor - total_flavor)
        if diff < min_diff:
            min_diff = diff
            optimal_flavor = flavor
    return optimal_flavor

