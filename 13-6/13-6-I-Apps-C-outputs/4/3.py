
def get_railway_network(n, m):
    # Function to get the railway network
    railway_network = []
    for i in range(m):
        u, v = map(int, input().split())
        railway_network.append((u, v))
    return railway_network

def get_road_network(n, m):
    # Function to get the road network
    road_network = []
    for i in range(m):
        u, v = map(int, input().split())
        road_network.append((u, v))
    return road_network

def get_min_time(railway_network, road_network, n):
    # Function to get the minimum time needed for both vehicles to reach town n
    min_time = -1
    for i in range(n):
        for j in range(i+1, n):
            if (i, j) in railway_network and (i, j) in road_network:
                min_time = max(min_time, 2)
            elif (i, j) in railway_network or (i, j) in road_network:
                min_time = max(min_time, 1)
    return min_time

def main():
    n, m = map(int, input().split())
    railway_network = get_railway_network(n, m)
    road_network = get_road_network(n, m)
    min_time = get_min_time(railway_network, road_network, n)
    print(min_time)

if __name__ == '__main__':
    main()

