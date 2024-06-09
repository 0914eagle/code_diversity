
def get_roads(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)

    # Find a Eulerian circuit in the graph
    circuit = []
    for i in range(n):
        if len(graph[i]) % 2 == 1:
            circuit.append(i)
            break
    else:
        return "NO"

    for i in range(n):
        if len(graph[circuit[i]]) == 0:
            continue
        j = graph[circuit[i]].pop()
        circuit.append(j)

    # Convert the Eulerian circuit to a sequence of roads
    roads = []
    for i in range(n-1):
        roads.append((circuit[i], circuit[i+1]))

    return "YES\n" + "\n".join(str(r[0]) + " " + str(r[1]) for r in roads)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_roads(n, a))

if __name__ == '__main__':
    main()

