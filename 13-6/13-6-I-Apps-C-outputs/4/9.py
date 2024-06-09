
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
    # Function to get the minimum time required for both vehicles to reach town n
    time = 0
    for i in range(n):
        if i == n-1:
            break
        for j in range(i+1, n):
            if (i, j) in railway_network or (j, i) in railway_network:
                time += 1
            elif (i, j) in road_network or (j, i) in road_network:
                time += 1
    return time

def main():
    n, m = map(int, input().split())
    railway_network = get_railway_network(n, m)
    road_network = get_road_network(n, m)
    print(get_min_time(railway_network, road_network, n))

if __name__ == '__main__':
    main()

