
def read_input():
    n = int(input())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))
    return n, table

def construct_map(n, table):
    map = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            map[i][j] = table[i][j]
    return map

def reconstruct_map(n, table):
    map = construct_map(n, table)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                map[i][j] = min(map[i][j], map[i][k] + map[k][j])
    return map

def find_roads(map):
    n = len(map)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if map[i][j] > 0:
                roads.append([i+1, j+1])
    return roads

def main():
    n, table = read_input()
    map = reconstruct_map(n, table)
    roads = find_roads(map)
    for road in roads:
        print(*road)

if __name__ == '__main__':
    main()

