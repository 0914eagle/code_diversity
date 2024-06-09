
def get_connected_roads(cities, roads):
    connected_roads = [0] * len(cities)
    for road in roads:
        city1, city2 = road
        connected_roads[city1 - 1] += 1
        connected_roads[city2 - 1] += 1
    return connected_roads

def main():
    cities, roads = read_input()
    connected_roads = get_connected_roads(cities, roads)
    print(*connected_roads, sep='\n')

def read_input():
    cities, roads = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(roads)]
    return cities, roads

if __name__ == '__main__':
    main()

