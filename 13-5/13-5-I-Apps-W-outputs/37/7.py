
def get_network_stations(n, a, b):
    # Initialize the number of stations needed
    num_stations = 0
    
    # Iterate through each city
    for i in range(n):
        # Calculate the total number of connections needed in the city
        total_connections = sum(a[i:i+1])
        
        # Calculate the number of stations needed for the city
        num_stations += (total_connections // b[i]) + (total_connections % b[i] > 0)
    
    return num_stations

def can_meet_needs(n, a, b):
    # Get the number of network stations needed
    num_stations = get_network_stations(n, a, b)
    
    # Return YES if the number of stations is greater than or equal to the number of cities
    return "YES" if num_stations >= n else "NO"

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        print(can_meet_needs(n, a, b))

