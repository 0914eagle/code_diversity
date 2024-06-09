
def solve(n, m, edges):
    # Initialize a dictionary to store the vertices and their neighbors
    neighbors = {}
    for i in range(1, n + 1):
        neighbors[i] = []

    # Add edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].append(edge[1])
        neighbors[edge[1]].append(edge[0])

    # Check if the graph is valid
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if j not in neighbors[i]:
                return "No"

    # Find a string that corresponds to the graph
    for string in itertools.product("abc", repeat=n):
        for i in range(n):
            for j in range(i + 1, n):
                if string[i] == string[j]:
                    break
            else:
                continue
            break
        else:
            return "Yes\n" + "".join(string)
    return "No"

