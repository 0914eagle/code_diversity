
def get_lipschitz_constant(points):
    max_diff = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            diff = abs(points[i][1] - points[j][1])
            max_diff = max(max_diff, diff)
    return max_diff

