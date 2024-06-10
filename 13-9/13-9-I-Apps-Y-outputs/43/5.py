
def get_roads(districts, gangs):
    # Initialize a graph with the districts as nodes
    graph = {i: set() for i in range(1, len(districts) + 1)}

    # Add edges between districts that belong to different gangs
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if gangs[i] != gangs[j]:
                graph[i].add(j)
                graph[j].add(i)

    # Find a path between every pair of districts
    paths = []
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            path = find_path(graph, i, j)
            if path:
                paths.append(path)

    # Check if all districts are reachable from each other
    reachable = set()
    for path in paths:
        reachable.update(path)
    if len(reachable) != len(districts):
        return "NO"

    # Check if all pairs of directly connected districts belong to different gangs
    for path in paths:
        i, j = path[0], path[-1]
        if gangs[i] == gangs[j]:
            return "NO"

    # Return the roads as a list of pairs of districts
    roads = []
    for path in paths:
        for i in range(len(path) - 1):
            roads.append((path[i], path[i + 1]))

    return "YES\n" + "\n".join(f"{i} {j}" for i, j in roads)

def find_path(graph, start, end):
    queue = [(start, [start])]
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        for neighbor in graph[current]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        num_districts = int(input())
        gangs = list(map(int, input().split()))
        print(get_roads(list(range(1, num_districts + 1)), gangs))

if __name__ == '__main__':
    main()

