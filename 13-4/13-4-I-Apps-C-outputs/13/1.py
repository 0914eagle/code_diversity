
def solve(s, r, f, t):
    # Initialize a graph with s nodes (states) and 2r + 2f edges
    graph = [[] for _ in range(s)]
    for i in range(r):
        graph[i].append(i + s)
        graph[i + s].append(i)
    for i in range(f):
        graph[i + s + r].append(i + s + r)
        graph[i].append(i + s + r)

    # Add edges for each transportation company
    for _ in range(t):
        n, *states = input().split()
        for i in range(int(n)):
            graph[states[i]].append(states[i + 1])

    # Find the maximum number of factories that can be supplied
    max_supply = 0
    for i in range(s):
        if len(graph[i]) == 1:
            max_supply += 1

    return max_supply

