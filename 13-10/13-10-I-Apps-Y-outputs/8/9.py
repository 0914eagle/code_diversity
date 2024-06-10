
def get_map(distances):
    n = len(distances)
    map = {}
    for i in range(n):
        for j in range(n):
            if i != j and distances[i][j] != 0:
                map[i, j] = distances[i][j]
    return map

def get_roads(map):
    n = len(map)
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if map[i, j] != 0:
                roads.append([i, j])
    return roads

def main():
    n = int(input())
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])
    map = get_map(distances)
    roads = get_roads(map)
    for road in roads:
        print("{} {}".format(*road))

if __name__ == '__main__':
    main()

