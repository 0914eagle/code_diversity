
def f1(n, c, encounters):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Find the earliest year in which all participants met
    years = [float('inf')] * (n + 1)
    for a in range(1, n + 1):
        for b, y in graph[a]:
            years[a] = min(years[a], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group has more than 2/3 of the participants
    for a in range(1, n + 1):
        if years[a] >= 2008:
            return 'Impossible'

    # Find the earliest year in which it is possible to divide the participants
    year = 2008
    while True:
        first_group = []
        second_group = []
        for a in range(1, n + 1):
            if years[a] < year:
                first_group.append(a)
            else:
                second_group.append(a)
        if len(first_group) > 2 * n / 3 or len(second_group) > 2 * n / 3:
            year += 1
        else:
            break

    return year

def f2(n, c, encounters):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))

    # Find the earliest year in which all participants met
    years = [float('inf')] * (n + 1)
    for a in range(1, n + 1):
        for b, y in graph[a]:
            years[a] = min(years[a], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group has more than 2/3 of the participants
    for a in range(1, n + 1):
        if years[a] >= 2008:
            return 'Impossible'

    # Find the earliest year in which it is possible to divide the participants
    year = 2008
    while True:
        first_group = []
        second_group = []
        for a in range(1, n + 1):
            if years[a] < year:
                first_group.append(a)
            else:
                second_group.append(a)
        if len(first_group) > 2 * n / 3 or len(second_group) > 2 * n / 3:
            year += 1
        else:
            break

    return year

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))
    print(f2(n, c, encounters))

