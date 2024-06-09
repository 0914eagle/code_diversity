
def get_network_stations(n, a, b):
    # Initialize the number of connections for each station
    connections = [0] * n
    # Iterate through each city and station
    for i in range(n):
        # Find the station with the least number of connections
        min_index = connections.index(min(connections))
        # If the current city requires more connections than the station can provide, return False
        if a[i] > b[min_index]:
            return False
        # Add the number of connections required by the current city to the station
        connections[min_index] += a[i]
    # If all cities have been assigned a station, return True
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print("YES") if get_network_stations(n, a, b) else print("NO")

if __name__ == '__main__':
    main()

