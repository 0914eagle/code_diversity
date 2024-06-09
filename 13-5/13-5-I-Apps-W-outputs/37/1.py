
def get_network_stations(n, a, b):
    
    # Initialize the list of network stations
    stations = []
    
    # Loop through each city and its neighboring city
    for i in range(n):
        # Get the number of households in the current city and its neighbor
        city_households = a[i]
        neighbor_households = a[(i+1)%n]
        
        # Check if the current city has more households than the capacity of the current network station
        if city_households > b[i]:
            # Add a new network station with the capacity of the current city
            stations.append(city_households)
        else:
            # Add the capacity of the current network station to the total number of households in the current city
            stations[-1] += b[i]
        
        # Check if the neighboring city has more households than the capacity of the current network station
        if neighbor_households > b[i]:
            # Add a new network station with the capacity of the neighboring city
            stations.append(neighbor_households)
        else:
            # Add the capacity of the current network station to the total number of households in the neighboring city
            stations[-1] += b[i]
    
    # Return the list of network stations
    return stations

def can_meet_needs(n, a, b):
    
    # Get the list of network stations
    stations = get_network_stations(n, a, b)
    
    # Initialize the total number of households to 0
    total_households = 0
    
    # Loop through each network station
    for station in stations:
        # Add the capacity of the current network station to the total number of households
        total_households += station
        
        # Check if the total number of households exceeds the total number of households in all cities
        if total_households > sum(a):
            # Return False
            return False
    
    # Return True
    return True

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the number of cities and their capacities
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        # Check if the designed network stations can meet the needs of all cities
        if can_meet_needs(n, a, b):
            # Print YES
            print("YES")
        else:
            # Print NO
            print("NO")

if __name__ == '__main__':
    main()

