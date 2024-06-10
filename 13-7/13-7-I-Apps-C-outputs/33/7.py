
def get_flight_changes(n, flights):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the flights
    for flight in flights:
        graph[flight[0] - 1].append(flight[1] - 1)
        graph[flight[1] - 1].append(flight[0] - 1)

    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    new_flight = None
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 1:
                changes = 0
                for k in range(n):
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        changes += 1
                if changes > max_changes:
                    max_changes = changes
                    flight_to_cancel = (i + 1, j + 1)
                    new_flight = (i + 1, j + 1)

    return max_changes, flight_to_cancel, new_flight

def main():
    n = int(input())
    flights = []
    for _ in range(n - 1):
        flights.append(tuple(map(int, input().split())))
    max_changes, flight_to_cancel, new_flight = get_flight_changes(n, flights)
    print(max_changes)
    print(*flight_to_cancel)
    print(*new_flight)

if __name__ == '__main__':
    main()

