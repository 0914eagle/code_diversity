
def find_bus_route(bus_routes, time_serval_goes_to_station):
    # Initialize a list to store the bus routes that arrive at the same time as Serval
    same_time_bus_routes = []
    
    # Iterate through the bus routes
    for bus_route in bus_routes:
        # Check if the first bus of the current route arrives at the same time as Serval
        if bus_route[0] == time_serval_goes_to_station:
            # If it does, add the route to the list of bus routes that arrive at the same time
            same_time_bus_routes.append(bus_route)
    
    # If there is only one bus route that arrives at the same time as Serval, return it
    if len(same_time_bus_routes) == 1:
        return same_time_bus_routes[0]
    # If there are multiple bus routes that arrive at the same time as Serval, return one of them randomly
    else:
        return same_time_bus_routes[0]

def main():
    # Read the input
    n, t = map(int, input().split())
    bus_routes = []
    for i in range(n):
        s, d = map(int, input().split())
        bus_routes.append([s, d])
    
    # Find the bus route that Serval will take
    bus_route = find_bus_route(bus_routes, t)
    
    # Print the bus route
    print(bus_route)

if __name__ == '__main__':
    main()

