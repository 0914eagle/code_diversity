
def get_roads(table):
    n = len(table)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if table[i][j] != 0:
                roads.append([i+1, j+1])
    return roads

def get_map(roads):
    n = len(roads)
    map = [[0 for _ in range(n)] for _ in range(n)]
    for road in roads:
        map[road[0]-1][road[1]-1] = 1
        map[road[1]-1][road[0]-1] = 1
    return map

def get_table(map):
    n = len(map)
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if map[i][j] == 1:
                table[i][j] = 1
                table[j][i] = 1
    return table

def main():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    roads = get_roads(table)
    map = get_map(roads)
    table = get_table(map)
    for road in roads:
        print(road[0], road[1])

if __name__ == '__main__':
    main()

