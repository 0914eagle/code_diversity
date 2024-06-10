
import itertools

def calculate_distance(distances, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def average_distance_between_signs(n, distances):
    total_distances = 0
    total_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_distances += calculate_distance(distances, [i, j])
            total_pairs += 1
    average_distance = total_distances / total_pairs
    return average_distance

if __name__ == "__main__":
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n - 1)]
    result = average_distance_between_signs(n, distances)
    print("{:.15f}".format(result))
