
def is_reasonable_network(n, m, friendships):
    # Initialize a dictionary to store the friends of each member
    friends = {i: set() for i in range(1, n + 1)}

    # Add the friendships to the dictionary
    for i in range(m):
        friends[friendships[i][0]].add(friendships[i][1])
        friends[friendships[i][1]].add(friendships[i][0])

    # Check if the network is reasonable
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i != j and j != k and k != i and (i in friends[j] and j in friends[k]) and (i not in friends[k]):
                    return "NO"

    return "YES"

