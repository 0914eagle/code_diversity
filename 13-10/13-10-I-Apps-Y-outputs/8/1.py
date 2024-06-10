
def get_distance_table(n):
    distance_table = []
    for i in range(n):
        distance_table.append([])
        for j in range(n):
            if i == j:
                distance_table[i].append(0)
            else:
                distance_table[i].append(int(input()))
    return distance_table

def get_minimum_spanning_tree(distance_table):
    n = len(distance_table)
    mst = []
    for i in range(n):
        for j in range(i+1, n):
            if distance_table[i][j] != 0 and distance_table[i][j] < distance_table[i][mst[-1]]:
                mst.append(j)
    return mst

def reconstruct_map(distance_table, mst):
    n = len(distance_table)
    map = []
    for i in range(n):
        for j in range(i+1, n):
            if distance_table[i][j] != 0 and (i, j) in mst:
                map.append((i, j))
    return map

def get_roads(map):
    roads = []
    for i in range(len(map)):
        roads.append((map[i][0], map[i][1]))
    return roads

def main():
    n = int(input())
    distance_table = get_distance_table(n)
    mst = get_minimum_spanning_tree(distance_table)
    map = reconstruct_map(distance_table, mst)
    roads = get_roads(map)
    for road in roads:
        print(road[0], road[1])

if __name__ == '__main__':
    main()

