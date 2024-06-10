
def get_input():
    n = int(input())
    flights = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        flights.append((a, b))
    return n, flights

def get_flight_changes(flights):
    n = len(flights) + 1
    graph = [[0] * n for _ in range(n)]
    for a, b in flights:
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1
    return graph

def get_flight_changes_matrix(graph):
    n = len(graph)
    changes = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                changes[i][j] = 1
            else:
                changes[i][j] = float('inf')
    for k in range(n):
        for i in range(n):
            for j in range(n):
                changes[i][j] = min(changes[i][j], changes[i][k] + changes[k][j])
    return changes

def get_optimal_flight(flight_changes):
    n = len(flight_changes)
    min_changes = float('inf')
    flight_to_cancel = None
    new_flight = None
    for i in range(n):
        for j in range(n):
            if flight_changes[i][j] < min_changes:
                min_changes = flight_changes[i][j]
                flight_to_cancel = (i + 1, j + 1)
                new_flight = (i + 1, j + 1)
    return min_changes, flight_to_cancel, new_flight

def main():
    n, flights = get_input()
    graph = get_flight_changes(flights)
    flight_changes = get_flight_changes_matrix(graph)
    min_changes, flight_to_cancel, new_flight = get_optimal_flight(flight_changes)
    print(min_changes)
    print(flight_to_cancel)
    print(new_flight)

if __name__ == '__main__':
    main()

