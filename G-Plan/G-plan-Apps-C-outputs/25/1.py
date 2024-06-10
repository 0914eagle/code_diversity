
def max_distance(towns, pairs, universities):
    def distance(u1, u2):
        return towns[u1][u2]

    def max_distance_recursive(univ, k, remaining):
        if k == 0:
            return 0
        max_sum = 0
        for i in range(len(remaining)):
            for j in range(i + 1, len(remaining)):
                u1, u2 = remaining[i], remaining[j]
                max_sum = max(max_sum, distance(univ[u1], univ[u2]) + max_distance_recursive(univ, k - 1, remaining[:i] + remaining[i + 1:j] + remaining[j + 1:]))
        return max_sum

    sorted_universities = sorted(universities)
    return max_distance_recursive(sorted_universities, pairs, list(range(len(universities))))

if __name__ == "__main__":
    n, k = map(int, input().split())
    towns = {}
    for _ in range(n - 1):
        x, y = map(int, input().split())
        if x not in towns:
            towns[x] = {}
        if y not in towns:
            towns[y] = {}
        towns[x][y] = 1
        towns[y][x] = 1
    universities = list(map(int, input().split()))
    print(max_distance(towns, k, universities))
