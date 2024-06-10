sum_distances(n, k, universities, roads):
    def calculate_distance(u1, u2):
        # Calculate distance between two universities
        # Assuming all roads have the same length of 1
        return roads[u1][u2]

    def divide_universities(universities, pairs, remaining):
        if pairs == 0:
            return 0

        max_distance = 0
        for i in range(len(remaining)):
            for j in range(i + 1, len(remaining)):
                u1, u2 = remaining[i], remaining[j]
                distance = calculate_distance(u1, u2)  # Calculate distance between universities
                new_remaining = remaining[:i] + remaining[i + 1:j] + remaining[j + 1:]
                max_distance = max(max_distance, distance + divide_universities(universities, pairs - 1, new_remaining))

        return max_distance

    universities.sort()
    return divide_universities(universities, k, universities)


if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = {i: {} for i in range(1, n + 1)}

    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads[x][y] = 1
        roads[y][x] = 1

    print(max_sum_distances(n, k, universities, roads)) 
