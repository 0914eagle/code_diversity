
def solve(N, M, K, onions, fence):
    # Calculate the convex hull of the fence posts
    hull = []
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    hull = set(hull)

    # Calculate the number of onions inside the convex hull
    num_onions = 0
    for i in range(N):
        if (onions[i][0], onions[i][1]) in hull:
            num_onions += 1

    # Return the maximum number of onions that can be protected
    return num_onions

