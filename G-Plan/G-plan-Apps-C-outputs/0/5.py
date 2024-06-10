
import itertools

def calculate_distance(distances, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def average_distance_signs(n, distances):
    total_pairs = n * (n - 1) // 2
    total_distance = 0
    count = 0

    for pair in itertools.combinations(range(n), 2):
        path = [pair[0]]
        while path[-1] != pair[1]:
            next_town = min(range(n), key=lambda x: distances[path[-1]][x] if x not in path else float('inf'))
            path.append(next_town)

        if len(path) == n:
            total_distance += calculate_distance(distances, path)
            count += 1

    if count == 0:
        print("impossible")
    else:
        print(total_distance / count)

if __name__ == "__main__":
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n - 1)]
    average_distance_signs(n, distances)
