
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
    for i in range(len(districts)):
        if len(graph[i]) == 1:
            circuit.append(i)
            graph[i].clear()
        for j in graph[i]:
            graph[j].remove(i)
            if len(graph[j]) == 0:
                circuit.append(j)
                graph[j].clear()

    # Convert the Eulerian circuit to a list of roads
    roads = []
    for i in range(len(circuit) - 1):
        roads.append((circuit[i], circuit[i + 1]))

    return roads

def main():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        gangs = list(map(int, input().split()))
        roads = get_roads(list(range(1, n + 1)), gangs)
        if len(roads) == n - 1:
            print("YES")
            for road in roads:
                print(*road)
        else:
            print("NO")

if __name__ == '__main__':
    main()

