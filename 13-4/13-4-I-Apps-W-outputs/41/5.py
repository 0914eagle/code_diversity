
def get_bus_route(bus_stops, time):
    # Find the first bus stop that arrives after the given time
    for i, stop in enumerate(bus_stops):
        if stop > time:
            return i
    # If all bus stops have arrived, return the last bus stop
    return len(bus_stops) - 1

def main():
    n, t = map(int, input().split())
    bus_stops = []
    for i in range(n):
        s, d = map(int, input().split())
        bus_stops.append(s + (i * d))
    print(get_bus_route(bus_stops, t))

if __name__ == '__main__':
    main()

