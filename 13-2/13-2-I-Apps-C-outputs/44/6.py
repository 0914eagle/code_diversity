
def solve(N, M, K, onions, fence_posts):
    # Calculate the convex hull of the fence posts
    hull = []
    for i in range(M):
        hull.append((fence_posts[i][0], fence_posts[i][1]))
    for i in range(M):
        hull.append((fence_posts[i][0], fence_posts[i][1]))
    hull = set(hull)

    # Calculate the number of onions that can be protected by each fence post
    protected_onions = [0] * M
    for i in range(N):
        if (onions[i][0], onions[i][1]) in hull:
            protected_onions[i] += 1

    # Sort the fence posts by the number of onions they protect
    sorted_fence_posts = sorted(range(M), key=lambda i: protected_onions[i], reverse=True)

    # Upgrade the first K fence posts to laser fence posts
    upgraded_fence_posts = sorted_fence_posts[:K]

    # Calculate the number of onions that can be protected by the upgraded fence posts
    protected_onions = [0] * M
    for i in range(N):
        if (onions[i][0], onions[i][1]) in hull:
            protected_onions[i] += 1

    # Return the maximum number of onions that can be protected
    return max(protected_onions)

