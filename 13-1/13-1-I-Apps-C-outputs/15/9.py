
def solve(N, K, M, edges):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a list to store the producers that can be left running
    producers = []

    # Iterate through each producer and check if it can be left running
    for producer in range(1, K + 1):
        # Initialize a set to store the conveyor belts that the producer uses
        conveyor_belts = set()

        # Iterate through each junction that the producer can reach
        for junction in graph[producer]:
            # If the junction is not the warehouse, add the conveyor belts that connect the junction to the warehouse
            if junction != N:
                conveyor_belts.update(graph[junction])

        # If the producer uses only one conveyor belt, it can be left running
        if len(conveyor_belts) == 1:
            producers.append(producer)

    return len(producers)

