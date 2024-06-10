
def read_input():
    n = int(input())
    flights = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        flights.append((a, b))
    return n, flights

def find_optimal_solution(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in flights:
        graph[a].add(b)
        graph[b].add(a)
    
    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if len(graph[a] & graph[b]) == 0:
                changes = 0
                for c in range(1, n + 1):
                    if c not in graph[a] and c not in graph[b]:
                        changes += 1
                if changes > max_changes:
                    max_changes = changes
                    flight_to_cancel = (a, b)
    
    # Find the best new flight to add
    best_new_flight = None
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if len(graph[a] & graph[b]) == 0:
                changes = 0
                for c in range(1, n + 1):
                    if c not in graph[a] and c not in graph[b]:
                        changes += 1
                if changes == max_changes:
                    best_new_flight = (a, b)
                    break
    
    return max_changes, flight_to_cancel, best_new_flight

def main():
    n, flights = read_input()
    max_changes, flight_to_cancel, best_new_flight = find_optimal_solution(n, flights)
    print(max_changes)
    print(*flight_to_cancel)
    print(*best_new_flight)

if __name__ == '__main__':
    main()

