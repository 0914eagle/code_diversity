distance(towns, universities, roads):
    def distance(u1, u2):
        return roads[u1][u2]

    universities.sort()
    n = len(universities)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            distances.append(distance(universities[i], universities[j]))

    distances.sort(reverse=True)
    return sum(distances[:towns // 2])


if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = {i: {} for i in range(1, n + 1)}
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads[x][y] = 1
        roads[y][x] = 1

    print(max_distance(n, universities, roads))
