
def get_network_stations(n, a, b):
    # Initialize the number of connections required for each city
    connections_required = a.copy()
    # Initialize the number of connections provided by each station
    connections_provided = [0] * n
    # Initialize the number of stations needed
    num_stations = 0
    
    # Loop through each city and station
    for i in range(n):
        # If the city requires more connections than the station can provide, add the difference to the total number of connections required
        if connections_required[i] > b[i]:
            connections_required[i] -= b[i]
            connections_required[(i+1)%n] += b[i]
        # If the city requires fewer connections than the station can provide, subtract the difference from the total number of connections provided
        else:
            connections_provided[i] += connections_required[i]
            connections_required[i] = 0
    
    # Loop through each city and check if it requires any connections
    for i in range(n):
        # If the city requires connections, add 1 to the number of stations needed
        if connections_required[i] > 0:
            num_stations += 1
    
    # Return the number of stations needed
    return num_stations

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the number of cities and stations
        n = int(input())
        
        # Read the number of households in each city
        a = list(map(int, input().split()))
        
        # Read the capacities of the stations
        b = list(map(int, input().split()))
        
        # Call the get_network_stations function to get the number of stations needed
        num_stations = get_network_stations(n, a, b)
        
        # Print YES if the number of stations needed is less than or equal to the number of stations available, otherwise print NO
        if num_stations <= n:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

