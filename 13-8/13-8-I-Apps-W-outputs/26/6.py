
def is_reasonable_network(n, m, friends):
    # Initialize a dictionary to store the friends of each member
    member_friends = {i: set() for i in range(1, n + 1)}
    # Add the friends of each member to the dictionary
    for friend in friends:
        member_friends[friend[0]].add(friend[1])
        member_friends[friend[1]].add(friend[0])
    # Check if the network is reasonable
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            for z in range(y + 1, n + 1):
                if (x, y) in friends and (y, z) in friends and (x, z) not in friends:
                    return "NO"
    return "YES"

