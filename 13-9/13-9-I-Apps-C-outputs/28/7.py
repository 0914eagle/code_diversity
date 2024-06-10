
def get_input():
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, k, universities, roads

def get_max_distance(universities, roads):
    # Initialize the graph with the universities as nodes
    graph = {university: set() for university in universities}

    # Add edges to the graph based on the roads
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])

    # Find the maximum distance by recursively searching for the longest path between universities
    max_distance = 0
    for university in universities:
        for other_university in universities:
            if university != other_university:
                distance = get_distance(graph, university, other_university)
                max_distance = max(max_distance, distance)

    return max_distance

def get_distance(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current == end:
                return distance
            for neighbor in graph[current]:
                queue.append((neighbor, distance + 1))
    return 0

def main():
    n, k, universities, roads = get_input()
    print(get_max_distance(universities, roads))

if __name__ == '__main__':
    main()

