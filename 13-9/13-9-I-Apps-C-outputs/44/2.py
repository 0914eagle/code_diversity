
def solve(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in flights:
        graph[i].add(j)
        graph[j].add(i)

    # Find the flight to cancel and the new flight to add
    flight_to_cancel, new_flight = None, None
    min_changes = float("inf")
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i != j and j not in graph[i]:
                # Find the number of changes needed when cancelling the flight (i, j)
                changes = 0
                queue = [i]
                visited = set()
                while queue:
                    node = queue.pop(0)
                    if node == j:
                        break
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                            changes += 1
                if changes < min_changes:
                    min_changes = changes
                    flight_to_cancel = (i, j)
                    new_flight = (j, i)

    return min_changes, flight_to_cancel, new_flight

