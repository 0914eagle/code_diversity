
def get_bus_route(n, t, bus_routes):
    # Initialize a list to store the bus routes that arrive at time t
    bus_routes_at_t = []
    
    # Iterate over the bus routes
    for i in range(n):
        # Get the time when the first bus of this route arrives and the interval between two buses of this route
        s_i, d_i = bus_routes[i]
        
        # Check if the first bus of this route arrives at time t
        if s_i == t:
            # If it does, add the route to the list of bus routes that arrive at time t
            bus_routes_at_t.append(i)
    
    # If there is only one bus route that arrives at time t, return it
    if len(bus_routes_at_t) == 1:
        return bus_routes_at_t[0]
    
    # If there are multiple bus routes that arrive at time t, return any of them randomly
    return bus_routes_at_t[0]

def main():
    # Read the input
    n, t = map(int, input().split())
    bus_routes = []
    for i in range(n):
        s_i, d_i = map(int, input().split())
        bus_routes.append((s_i, d_i))
    
    # Call the function to get the bus route that Serval will use
    bus_route = get_bus_route(n, t, bus_routes)
    
    # Print the bus route
    print(bus_route)

if __name__ == '__main__':
    main()

