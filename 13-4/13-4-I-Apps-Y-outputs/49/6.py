
def get_connected_roads(n_cities, roads):
    connected_roads = [0] * n_cities
    for road in roads:
        connected_roads[road[0] - 1] += 1
        connected_roads[road[1] - 1] += 1
    return connected_roads

def main():
    n_cities, n_roads = map(int, input().split())
    roads = []
    for _ in range(n_roads):
        roads.append(list(map(int, input().split())))
    connected_roads = get_connected_roads(n_cities, roads)
    for road in connected_roads:
        print(road)

if __name__ == '__main__':
    main()

