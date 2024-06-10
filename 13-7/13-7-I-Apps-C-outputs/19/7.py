
def divide_participants(n, c, encounters):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the known encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Sort the edges in non-decreasing order of their year
    for neighbors in graph:
        neighbors.sort(key=lambda x: x[1])

    # Initialize the minimum year as the latest year in the encounters
    min_year = max(year for _, _, year in encounters)

    # Iterate through the years in non-decreasing order
    for year in range(min_year, 2008):
        # Initialize two empty sets to store the first and second parts
        first_part = set()
        second_part = set()

        # Iterate through the vertices in the graph
        for vertex in range(1, n + 1):
            # If the vertex is not in either part, add it to the first part
            if vertex not in first_part and vertex not in second_part:
                first_part.add(vertex)

            # If the vertex is in the first part and has an edge to a vertex in the second part, move the vertex to the second part
            elif vertex in first_part and any(neighbor in second_part for neighbor, _ in graph[vertex]):
                first_part.remove(vertex)
                second_part.add(vertex)

        # If both parts contain at most 2/3 of the vertices, return the year
        if len(first_part) + len(second_part) <= 2 * n / 3:
            return year

    # If no year is found, return 'Impossible'
    return 'Impossible'

def main():
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(divide_participants(n, c, encounters))

if __name__ == '__main__':
    main()

