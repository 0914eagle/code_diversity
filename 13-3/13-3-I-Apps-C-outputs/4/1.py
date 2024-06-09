
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a dictionary to store the number of lounges at each airport
    airport_lounges = {i: 0 for i in range(1, n_airports + 1)}
    
    # Iterate over the routes and update the number of lounges at each airport
    for route in routes:
        airport1, airport2, lounges = route
        airport_lounges[airport1] += lounges
        airport_lounges[airport2] += lounges
    
    # Initialize the minimum number of lounges needed to be built
    min_lounges = 0
    
    # Iterate over the airports and check if the number of lounges at each airport is valid
    for airport, lounges in airport_lounges.items():
        if lounges == 0:
            continue
        elif lounges == 1:
            min_lounges += 1
        elif lounges == 2:
            min_lounges += 2
        else:
            return "impossible"
    
    return min_lounges

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

