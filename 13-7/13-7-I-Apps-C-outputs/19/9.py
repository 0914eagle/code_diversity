
def is_possible(n, c, encounters):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Find the earliest year when all participants met for the first time
    earliest_year = 2008
    for node in graph:
        for neighbor, year in node:
            earliest_year = min(earliest_year, year)

    # Divide the participants into two groups
    group1 = set()
    group2 = set()
    for node in graph:
        if node[0][1] < earliest_year:
            group1.add(node[0][0])
        else:
            group2.add(node[0][0])

    # Check if both groups have at most 2/3 of the participants
    if len(group1) > 2 * n / 3 or len(group2) > 2 * n / 3:
        return "Impossible"

    # Return the earliest year
    return earliest_year

def main():
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(is_possible(n, c, encounters))

if __name__ == '__main__':
    main()

