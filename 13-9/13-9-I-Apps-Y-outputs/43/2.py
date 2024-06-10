
def get_roads(districts, gangs):
    # Initialize a graph with the districts as nodes
    graph = {i: set() for i in range(1, len(districts) + 1)}

    # Add edges to the graph based on the gang affiliations
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if gangs[i] != gangs[j]:
                graph[i].add(j)
                graph[j].add(i)

    # Find all reachable districts from each district
    reachable = {i: set() for i in range(1, len(districts) + 1)}
    for i in range(len(districts)):
        queue = [i]
        while queue:
            curr = queue.pop(0)
            reachable[i].add(curr)
            queue.extend(graph[curr] - reachable[i])

    # Check if all districts are reachable from each other
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if i not in reachable[j] or j not in reachable[i]:
                return "NO"

    # Build the roads
    roads = []
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if gangs[i] != gangs[j]:
                roads.append([i, j])

    return "YES\n" + "\n".join(str(road[0]) + " " + str(road[1]) for road in roads)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        gangs = list(map(int, input().split()))
        print(get_roads(list(range(1, n + 1)), gangs))

if __name__ == '__main__':
    main()

