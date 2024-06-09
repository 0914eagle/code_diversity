
def get_roads(districts, gangs):
    # Initialize a graph with the districts as nodes
    graph = {i: set() for i in range(1, len(districts) + 1)}

    # Add edges to the graph based on the gangs
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if gangs[i] != gangs[j]:
                graph[i].add(j)
                graph[j].add(i)

    # Find all connected components in the graph
    connected_components = []
    visited = set()
    for i in range(1, len(districts) + 1):
        if i not in visited:
            component = []
            dfs(graph, i, visited, component)
            connected_components.append(component)

    # Check if all districts are connected
    if len(connected_components) == 1:
        return "YES"
    else:
        return "NO"

def dfs(graph, start, visited, component):
    visited.add(start)
    component.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def main():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        districts = list(map(int, input().split()))
        gangs = list(map(int, input().split()))
        print(get_roads(districts, gangs))

if __name__ == '__main__':
    main()

