
def solve(N, M, K, onions, fence):
    # Calculate the convex hull of the fence posts
    hull = []
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    for i in range(M):
        hull.append((fence[i][0], fence[i][1]))
    hull = set(hull)

    # Initialize the maximum number of onions to protect as 0
    max_onions = 0

    # Iterate through all possible combinations of fence posts to upgrade
    for combination in combinations(range(M), K):
        # Calculate the convex hull of the selected fence posts
        selected_hull = []
        for i in combination:
            selected_hull.append((fence[i][0], fence[i][1]))
        selected_hull = set(selected_hull)

        # Count the number of onions within the selected convex hull
        num_onions = 0
        for onion in onions:
            if (onion[0], onion[1]) in selected_hull:
                num_onions += 1

        # Update the maximum number of onions if necessary
        if num_onions > max_onions:
            max_onions = num_onions

    return max_onions

