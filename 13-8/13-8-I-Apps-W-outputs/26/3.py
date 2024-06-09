
def is_network_reasonable(n, m, edges):
    # Initialize a dictionary to store the friends of each member
    friends = {i: set() for i in range(1, n + 1)}

    # Add the given edges to the dictionary
    for edge in edges:
        friends[edge[0]].add(edge[1])
        friends[edge[1]].add(edge[0])

    # Check if the network is reasonable
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if x != y and y != z and x != z:
                    if (x in friends[y] and y in friends[z]) and (x not in friends[z]):
                        return "NO"

    return "YES"

