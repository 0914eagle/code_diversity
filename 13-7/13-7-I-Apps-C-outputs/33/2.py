
def get_flight_changes(flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, len(flights) + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])
    
    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    for flight in flights:
        changes = 0
        queue = [flight[0]]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node == flight[1]:
                break
            for neighbor in graph[node] - visited:
                queue.append(neighbor)
                visited.add(neighbor)
            changes += 1
        if changes > max_changes:
            max_changes = changes
            flight_to_cancel = flight
    
    # Find the flight to add to minimize the number of changes
    min_changes = max_changes
    flight_to_add = None
    for i in range(1, len(flights) + 1):
        for j in range(i + 1, len(flights) + 1):
            if i != j and (i, j) not in flights and (j, i) not in flights:
                changes = 0
                queue = [i]
                visited = set()
                while queue:
                    node = queue.pop(0)
                    if node == j:
                        break
                    for neighbor in graph[node] - visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                    changes += 1
                if changes < min_changes:
                    min_changes = changes
                    flight_to_add = (i, j)
    
    return min_changes, flight_to_cancel, flight_to_add

def main():
    flights = []
    for _ in range(int(input())):
        flights.append(tuple(map(int, input().split())))
    min_changes, flight_to_cancel, flight_to_add = get_flight_changes(flights)
    print(min_changes)
    print(*flight_to_cancel)
    print(*flight_to_add)

if __name__ == '__main__':
    main()

