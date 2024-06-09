
def get_average_distance(n, distances):
    # Calculate the total distance between all pairs of port towns
    total_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            total_distance += distances[i][j]

    # Calculate the average distance between all pairs of port towns
    average_distance = total_distance / (n * (n - 1))

    return average_distance

