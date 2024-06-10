
def calculate_average_distance(n, distances):
    total_distance = 0
    total_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            total_distance += distances[i][j - i - 1]
            total_pairs += 1

    average_distance = total_distance / total_pairs if total_pairs > 0 else "impossible"
    return average_distance

if __name__ == "__main__":
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n - 1)]

    result = calculate_average_distance(n, distances)
    print(result)
