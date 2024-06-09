
def f1(n, roads):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1])
        graph[road[1] - 1].append(road[0])

    # Find a Eulerian circuit in the graph
    eulerian_circuit = []
    for vertex in range(n):
        if len(graph[vertex]) % 2 == 1:
            eulerian_circuit.append(vertex + 1)
            break

    # Construct the output
    output = []
    for i in range(len(eulerian_circuit) - 1):
        output.append([eulerian_circuit[i], eulerian_circuit[i + 1]])

    return output

def f2(n, roads):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        graph[road[0] - 1].append(road[1])
        graph[road[1] - 1].append(road[0])

    # Find a Eulerian path in the graph
    eulerian_path = []
    for vertex in range(n):
        if len(graph[vertex]) % 2 == 1:
            eulerian_path.append(vertex + 1)
            break

    # Construct the output
    output = []
    for i in range(len(eulerian_path) - 1):
        output.append([eulerian_path[i], eulerian_path[i + 1]])

    return output

if __name__ == '__main__':
    n = int(input())
    roads = []
    for _ in range(n):
        roads.append(list(map(int, input().split())))

    output = f1(n, roads)
    for road in output:
        print(road[0], road[1])

