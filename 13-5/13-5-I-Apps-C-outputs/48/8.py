
def f1(n, c, encounters):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a - 1].append((b - 1, y))
        graph[b - 1].append((a - 1, y))

    # Find the earliest year in which all participants met
    years = [float('inf')] * n
    for i in range(n):
        for j, y in graph[i]:
            years[i] = min(years[i], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group contains more than 2/3 of the participants
    for i in range(n):
        if years[i] != float('inf'):
            break
    else:
        return 'Impossible'

    # Divide the participants into two groups based on their earliest meeting years
    group1 = [i for i in range(n) if years[i] < years[i - 1]]
    group2 = [i for i in range(n) if years[i] >= years[i - 1]]

    # Check if the two groups contain no more than 2/3 of the participants
    if len(group1) > 2 * n // 3 or len(group2) > 2 * n // 3:
        return 'Impossible'

    # Return the smallest year in which it is possible to divide the participants
    return min(years)

def f2(n, c, encounters):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a - 1].append((b - 1, y))
        graph[b - 1].append((a - 1, y))

    # Find the earliest year in which all participants met
    years = [float('inf')] * n
    for i in range(n):
        for j, y in graph[i]:
            years[i] = min(years[i], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group contains more than 2/3 of the participants
    for i in range(n):
        if years[i] != float('inf'):
            break
    else:
        return 'Impossible'

    # Divide the participants into two groups based on their earliest meeting years
    group1 = [i for i in range(n) if years[i] < years[i - 1]]
    group2 = [i for i in range(n) in range(n) if years[i] >= years[i - 1]]

    # Check if the two groups contain no more than 2/3 of the participants
    if len(group1) > 2 * n // 3 or len(group2) > 2 * n // 3:
        return 'Impossible'

    # Return the smallest year in which it is possible to divide the participants
    return min(years)

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))
    print(f2(n, c, encounters))

