
def solve(N, M, K, onions, fence):
    # Calculate the convex hull of the fence posts
    hull = []
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    hull = set(hull)

    # Calculate the area of each onion
    areas = []
    for i in range(N):
        area = 0
        for j in range(M):
            area += (fence[j][0] - onions[i][0]) * (fence[j][1] - onions[i][1])
        areas.append(area)

    # Sort the onions by area in descending order
    sorted_areas = sorted(areas, reverse=True)

    # Upgrade the fence posts to protect the onions with the largest areas
    upgraded_posts = set()
    for i in range(K):
        upgraded_posts.add(sorted_areas[i])

    # Calculate the number of onions protected by the upgraded fence posts
    protected_onions = 0
    for i in range(N):
        if (onions[i][0], onions[i][1]) in upgraded_posts:
            protected_onions += 1

    return protected_onions

