
def read_input():
    n, s, t, q = map(int, input().split())
    hills = []
    for _ in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    springs = list(map(int, input().split()))
    towns = list(map(int, input().split()))
    return n, s, t, q, hills, springs, towns

def find_path(start, end, path, visited, graph):
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            new_path = find_path(neighbor, end, path + [neighbor], visited, graph)
            if new_path:
                return new_path
    return []

def get_possible_paths(start, end, graph):
    visited = set()
    return find_path(start, end, [start], visited, graph)

def construct_graph(hills):
    graph = {}
    for i in range(len(hills)):
        graph[i] = []
    for i in range(len(hills)):
        for j in range(i + 1, len(hills)):
            if hills[i][2] < hills[j][2]:
                graph[i].append(j)
    return graph

def get_spring_town_paths(springs, towns, graph):
    spring_town_paths = []
    for spring in springs:
        for town in towns:
            path = get_possible_paths(spring, town, graph)
            if path:
                spring_town_paths.append(path)
    return spring_town_paths

def get_spring_spring_paths(springs, graph):
    spring_spring_paths = []
    for spring in springs:
        for other_spring in springs:
            if spring != other_spring:
                path = get_possible_paths(spring, other_spring, graph)
                if path:
                    spring_spring_paths.append(path)
    return spring_spring_paths

def get_total_length(spring_town_paths, spring_spring_paths):
    total_length = 0
    for path in spring_town_paths:
        length = 0
        for i in range(len(path) - 1):
            hill1 = path[i]
            hill2 = path[i + 1]
            length += get_distance(hills[hill1], hills[hill2])
        total_length += length
    for path in spring_spring_paths:
        length = 0
        for i in range(len(path) - 1):
            hill1 = path[i]
            hill2 = path[i + 1]
            length += get_distance(hills[hill1], hills[hill2])
        total_length += length
    return total_length

def get_distance(hill1, hill2):
    return ((hill1[0] - hill2[0]) ** 2 + (hill1[1] - hill2[1]) ** 2) ** 0.5

def main():
    n, s, t, q, hills, springs, towns = read_input()
    graph = construct_graph(hills)
    spring_town_paths = get_spring_town_paths(springs, towns, graph)
    spring_spring_paths = get_spring_spring_paths(springs, graph)
    total_length = get_total_length(spring_town_paths, spring_spring_paths)
    print(total_length)

if __name__ == '__main__':
    main()

