
def solve(N, M, K, onions, fence):
    # Calculate the convex hull of the fence posts
    hull = []
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    hull = set(hull)

    # Calculate the number of onions that can be protected by each fence post
    protected_onions = [0] * M
    for i in range(N):
        for j in range(M):
            if (onions[i][0], onions[i][1]) in hull:
                protected_onions[j] += 1

    # Sort the fence posts by the number of onions they protect
    sorted_fence = sorted(range(M), key=lambda x: protected_onions[x], reverse=True)

    # Upgrade the first K fence posts
    upgraded_fence = sorted_fence[:K]

    # Calculate the number of onions that can be protected by the upgraded fence
    protected_onions = 0
    for i in range(N):
        for j in range(K):
            if (onions[i][0], onions[i][1]) in hull:
                protected_onions += 1
                break

    return protected_onions

