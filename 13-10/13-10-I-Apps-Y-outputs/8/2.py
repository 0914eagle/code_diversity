
def get_shortest_path(table):
    n = len(table)
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for i in range(n):
        for j in range(i+1, n):
            distances[i][j] = min(distances[i][j], table[i][j])
            distances[j][i] = min(distances[j][i], table[i][j])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances

def get_roads(table):
    n = len(table)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != float('inf'):
                roads.append([i+1, j+1])
    return roads

def main():
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    distances = get_shortest_path(table)
    roads = get_roads(distances)
    for road in roads:
        print(' '.join(map(str, road)))

if __name__ == '__main__':
    main()

