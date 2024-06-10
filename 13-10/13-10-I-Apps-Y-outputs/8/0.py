
def find_distance(table):
    n = len(table)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = table[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def find_roads(dist):
    n = len(dist)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if dist[i][j] != 0 and dist[i][j] != float('inf'):
                roads.append([i+1, j+1])
    return roads

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    dist = find_distance(table)
    roads = find_roads(dist)
    for road in roads:
        print('{} {}'.format(road[0], road[1]))

if __name__ == '__main__':
    main()

