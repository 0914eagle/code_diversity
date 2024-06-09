
def get_network_stations(n, a, b):
    # Initialize the number of connections for each station
    connections = [0] * n
    # Loop through each city and station
    for i in range(n):
        # Calculate the number of connections for the current station
        connections[i] = min(b[i], a[i])
        # Subtract the number of connections from the previous station
        if i > 0:
            connections[i] -= connections[i - 1]
    # Return the number of connections for each station
    return connections

def can_meet_needs(n, a, b):
    # Get the number of connections for each station
    connections = get_network_stations(n, a, b)
    # Check if the total number of connections is sufficient
    return sum(connections) >= sum(a)

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
        # Check if the stations can meet the needs of all cities
        if can_meet_needs(n, a, b):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

