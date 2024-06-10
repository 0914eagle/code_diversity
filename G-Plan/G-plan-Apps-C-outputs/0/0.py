
def calculate_distance(i, j, distances):
    return distances[min(i, j)][abs(i - j)]

def calculate_average_distance(n, distances):
    total_distance = 0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_distance += calculate_distance(i, j, distances)
            count += 1
    return total_distance / count if count > 0 else "impossible"

if __name__ == "__main__":
    n = int(input())
    distances = [list(map(int, input().split())) for _ in range(n - 1)]
    result = calculate_average_distance(n, distances)
    print(result)
