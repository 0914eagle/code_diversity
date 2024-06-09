
def get_roads(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]
    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)
    # Find all connected components in the graph
    connected_components = []
    for i in range(n):
        if not graph[i]:
            continue
        component = [i]
        queue = [i]
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in component:
                    component.append(neighbor)
                    queue.append(neighbor)
        connected_components.append(component)
    # Check if all districts are reachable from each other
    if len(connected_components) > 1:
        return "NO"
    # Build roads between connected components
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                roads.append([i, j])
    return "YES\n" + "\n".join(str(road[0]) + " " + str(road[1]) for road in roads)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_roads(n, a))

if __name__ == '__main__':
    main()

