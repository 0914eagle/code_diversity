
def get_average_distance(n, distances):
    # Calculate the average distance between all pairs of port towns
    average_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            average_distance += distances[i][j]
    average_distance /= (n * (n - 1)) / 2

    # Calculate the average distance between all pairs of distance signs
    total_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            total_distance += distances[i][j]
    average_distance_signs = total_distance / (n * (n - 1))

    return average_distance_signs

