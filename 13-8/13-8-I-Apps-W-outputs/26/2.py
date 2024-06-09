
def is_reasonable_network(n, m, friends):
    # Initialize a dictionary to store the friends of each member
    friend_dict = {i: set() for i in range(1, n + 1)}

    # Add the friends to the dictionary
    for i in range(m):
        friend_dict[friends[i][0]].add(friends[i][1])
        friend_dict[friends[i][1]].add(friends[i][0])

    # Check if the network is reasonable
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if (i in friend_dict[j] and j in friend_dict[k]) and (i not in friend_dict[k]):
                    return "NO"

    return "YES"

