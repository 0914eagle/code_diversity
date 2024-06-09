
def find_bus_route(t, bus_routes):
    # Find the first bus route that has a bus arriving at or after the given time t
    for i, route in enumerate(bus_routes):
        if route[0] <= t:
            return i + 1
    return -1

def main():
    n, t = map(int, input().split())
    bus_routes = []
    for i in range(n):
        s, d = map(int, input().split())
        bus_routes.append((s, d))
    print(find_bus_route(t, bus_routes))

if __name__ == '__main__':
    main()

