
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a dictionary to store the number of lounges at each airport
    airport_lounges = {i: 0 for i in range(1, n_airports + 1)}
    
    # Iterate over the routes and update the number of lounges at each airport
    for route in routes:
        airport1, airport2, lounges = route
        airport_lounges[airport1] += lounges
        airport_lounges[airport2] += lounges
    
    # Initialize a set to store the airports with at least one lounge
    lounged_airports = set()
    
    # Iterate over the airports and check if they have at least one lounge
    for airport, lounges in airport_lounges.items():
        if lounges > 0:
            lounged_airports.add(airport)
    
    # If all airports have at least one lounge, return the total number of lounges
    if len(lounged_airports) == n_airports:
        return sum(airport_lounges.values())
    
    # If not all airports have at least one lounge, return "impossible"
    return "impossible"

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

