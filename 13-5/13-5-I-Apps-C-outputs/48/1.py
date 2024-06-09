
def f1(n, c, encounters):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a - 1].append((b - 1, y))
        graph[b - 1].append((a - 1, y))

    # Find the earliest year in which all participants met each other
    years = [float('inf')] * n
    for i in range(n):
        for j, y in graph[i]:
            years[i] = min(years[i], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group contains more than 2/3 of the participants
    # and all participants in one group met each other before the chosen year
    # and all participants in the other group met each other after the chosen year
    for y in range(1948, 2008 + 1):
        group1 = set()
        group2 = set(range(n))
        for i in range(n):
            if years[i] <= y:
                group1.add(i)
                group2.remove(i)
            if len(group1) > 2 * n / 3 or len(group2) > 2 * n / 3:
                break
        else:
            return y
    return 'Impossible'

def f2(n, c, encounters):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a - 1].append((b - 1, y))
        graph[b - 1].append((a - 1, y))

    # Find the earliest year in which all participants met each other
    years = [float('inf')] * n
    for i in range(n):
        for j, y in graph[i]:
            years[i] = min(years[i], y)

    # Check if it is possible to divide the participants into two groups
    # such that no group contains more than 2/3 of the participants
    # and all participants in one group met each other before the chosen year
    # and all participants in the other group met each other after the chosen year
    for y in range(1948, 2008 + 1):
        group1 = set()
        group2 = set(range(n))
        for i in range(n):
            if years[i] <= y:
                group1.add(i)
                group2.remove(i)
            if len(group1) > 2 * n / 3 or len(group2) > 2 * n / 3:
                break
        else:
            return y
    return 'Impossible'

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))
    print(f2(n, c, encounters))

