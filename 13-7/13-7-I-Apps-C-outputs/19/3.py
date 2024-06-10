
def get_dinner_partners(n, c, encounters):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Initialize the year Y to be the maximum year in the encounters
    Y = max(encounters, key=lambda x: x[2])[2]

    # Initialize the two parts of the dinner
    part1 = []
    part2 = []

    # Iterate through the vertices of the graph
    for i in range(1, n + 1):
        # If the vertex has not been visited, visit it and add it to the appropriate part
        if i not in part1 and i not in part2:
            if visit(graph, i, Y, part1, part2):
                return Y

    # If no year Y exists, return 'Impossible'
    return 'Impossible'

def visit(graph, i, Y, part1, part2):
    # If the vertex is in the first part, add it to the second part
    if i in part1:
        part2.append(i)
    # If the vertex is in the second part, add it to the first part
    elif i in part2:
        part1.append(i)
    # If the vertex has not been visited, visit it and add it to the appropriate part
    else:
        # If the vertex has an edge to a vertex in the first part, add it to the second part
        if any(j in part1 for j, y in graph[i] if y <= Y):
            part2.append(i)
        # If the vertex has an edge to a vertex in the second part, add it to the first part
        elif any(j in part2 for j, y in graph[i] if y > Y):
            part1.append(i)
        # If the vertex has no edges to either part, visit it and add it to the appropriate part
        else:
            if visit(graph, i, Y, part1, part2):
                return True

    # If the two parts have more than 2/3 of the vertices, return False
    if len(part1) + len(part2) > 2 * n / 3:
        return False
    # If the two parts have exactly 2/3 of the vertices, return True
    elif len(part1) + len(part2) == 2 * n / 3:
        return True
    # If the two parts have less than 2/3 of the vertices, continue visiting vertices
    else:
        return True

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(get_dinner_partners(n, c, encounters))

