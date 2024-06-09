
def f1(n, m, k):
    # find the shortest path between all pairs of cities
    # using Floyd-Warshall algorithm
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(m):
        u, v, l = map(int, input().split())
        dist[u-1][v-1] = l
        dist[v-1][u-1] = l
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # find the minimum cost of opening a bakery in each city
    # and the city with the minimum cost
    cost = [float('inf') for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf'):
                cost[i] = min(cost[i], dist[i][j])
    min_cost = min(cost)
    min_city = cost.index(min_cost)
    return min_city + 1

def f2(n, m, k, a):
    # find the shortest path between the bakery and the storage
    # using Floyd-Warshall algorithm
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(m):
        u, v, l = map(int, input().split())
        dist[u-1][v-1] = l
        dist[v-1][u-1] = l
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # find the minimum cost of opening a bakery in each city
    # and the city with the minimum cost
    cost = [float('inf') for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf'):
                cost[i] = min(cost[i], dist[i][j])
    min_cost = min(cost)
    min_city = cost.index(min_cost)
    return min_city + 1

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_city = f1(n, m, k)
    if min_city == -1:
        print(-1)
    else:
        print(f2(n, m, k, a))

