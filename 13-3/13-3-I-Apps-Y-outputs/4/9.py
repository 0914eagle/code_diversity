
def get_roads(districts, gangs):
    # Initialize a graph with the districts as nodes
    graph = {i: set() for i in range(1, len(districts) + 1)}

    # Add edges to the graph based on the gangs
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if gangs[i] != gangs[j]:
                graph[i].add(j)
                graph[j].add(i)

    # Find a Eulerian circuit in the graph
    circuit = []
    for node in range(1, len(districts) + 1):
        if node not in circuit:
            dfs(graph, node, circuit)

    # Convert the Eulerian circuit to a list of roads
    roads = []
    for i in range(len(circuit) - 1):
        roads.append((circuit[i], circuit[i + 1]))

    return roads

def dfs(graph, node, circuit):
    if node in circuit:
        return
    circuit.append(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, circuit)

def main():
    tests = int(input())
    for test in range(tests):
        n = int(input())
        gangs = list(map(int, input().split()))
        districts = list(range(1, n + 1))
        roads = get_roads(districts, gangs)
        if len(roads) == n - 1:
            print("YES")
            for road in roads:
                print(*road)
        else:
            print("NO")

if __name__ == '__main__':
    main()

