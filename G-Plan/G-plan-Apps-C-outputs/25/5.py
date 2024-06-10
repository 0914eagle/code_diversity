distance(towns, pairs, universities, roads):
    def distance(u1, u2):
        return roads[u1][u2]

    universities.sort()
    n = len(universities)
    dp = [[-1] * (pairs + 1) for _ in range(n)]

    def solve(idx, pairs_left):
        if idx == n:
            return 0
        if dp[idx][pairs_left] != -1:
            return dp[idx][pairs_left]

        res = 0
        for i in range(idx + 1, n):
            res = max(res, distance(universities[idx], universities[i]) + solve(i, pairs_left - 1))

        dp[idx][pairs_left] = res
        return res

    return solve(0, pairs)


if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = {}
    for _ in range(n - 1):
        x, y = map(int, input().split())
        if x not in roads:
            roads[x] = {}
        if y not in roads:
            roads[y] = {}
        roads[x][y] = 1
        roads[y][x] = 1

    print(max_distance(n, k, universities, roads)) 
