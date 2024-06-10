
from itertools import combinations

def calculate_distance(distance_table, pair):
    total_distance = 0
    for i in range(len(pair) - 1):
        total_distance += distance_table[pair[i]][pair[i + 1]]
    return total_distance

def calculate_average_distance(n, distances):
    distance_table = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(n - i - 1):
            distance_table[i][i + j + 1] = distances[i][j]
            distance_table[i + j + 1][i] = distances[i][j]

    total_distances = 0
    total_pairs = 0
    for pair in combinations(range(n), 2):
        distance = calculate_distance(distance_table, pair)
        if distance == 0:
            return "impossible"
        total_distances += distance
        total_pairs += 1

    return total_distances / total_pairs

if __name__ == "__main__":
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n - 1)]
    result = calculate_average_distance(n, distances)
    print(result)
