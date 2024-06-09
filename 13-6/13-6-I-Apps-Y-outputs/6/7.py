
def get_satisfaction_points(n, dishes, satisfaction_points, extra_satisfaction_points):
    points = 0
    for i in range(n):
        points += satisfaction_points[i]
        if i < n - 1 and dishes[i] == dishes[i + 1] - 1:
            points += extra_satisfaction_points[i]
    return points

