
def is_network_reasonable(n, m, edges):
    # Initialize a dictionary to store the friends of each member
    friends = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        friends[edge[0]].add(edge[1])
        friends[edge[1]].add(edge[0])

    # Check if the network is reasonable
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if (i in friends[j]) and (j in friends[k]) and (i not in friends[k]):
                    return "NO"

    return "YES"

