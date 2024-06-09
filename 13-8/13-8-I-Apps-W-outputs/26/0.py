
def is_reasonable_network(n, m, edges):
    # Initialize a dictionary to store the friends of each member
    friends = {i: set() for i in range(1, n + 1)}

    # Add the given edges to the dictionary
    for edge in edges:
        friends[edge[0]].add(edge[1])
        friends[edge[1]].add(edge[0])

    # Check if the network is reasonable
    for x, y, z in combinations(friends, 3):
        if x != y and y != z and x != z:
            if not (y in friends[x] and z in friends[y] and x in friends[z]):
                return "NO"

    return "YES"

