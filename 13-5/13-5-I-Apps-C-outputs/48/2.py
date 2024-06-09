
def f1(n, c, encounters):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Find the earliest year where all participants met at least once
    years = set()
    for node in graph:
        for neighbor, year in node:
            years.add(year)
    earliest_year = min(years)

    # Check if it is possible to divide the participants into two groups
    # such that no group has more than 2/3 of the participants and
    # all participants in the first group first met before the earliest year
    # and all participants in the second group first met in or after the earliest year
    for group_size in range(1, n // 2 + 1):
        if n % group_size == 0:
            first_group = set(range(1, group_size + 1))
            second_group = set(range(group_size + 1, n + 1))
            if all(year <= earliest_year for node in first_group for neighbor, year in graph[node] if neighbor in second_group):
                return earliest_year

    return "Impossible"

def f2(n, c, encounters):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Find the earliest year where all participants met at least once
    years = set()
    for node in graph:
        for neighbor, year in node:
            years.add(year)
    earliest_year = min(years)

    # Check if it is possible to divide the participants into two groups
    # such that no group has more than 2/3 of the participants and
    # all participants in the first group first met before the earliest year
    # and all participants in the second group first met in or after the earliest year
    for group_size in range(1, n // 2 + 1):
        if n % group_size == 0:
            first_group = set(range(1, group_size + 1))
            second_group = set(range(group_size + 1, n + 1))
            if all(year <= earliest_year for node in first_group for neighbor, year in graph[node] if neighbor in second_group):
                return earliest_year

    return "Impossible"

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))
    print(f2(n, c, encounters))

