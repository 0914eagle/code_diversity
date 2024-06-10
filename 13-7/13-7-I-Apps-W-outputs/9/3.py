
def get_friends(m, k, friend_pairs):
    # Initialize a dictionary to store the friends of each user
    friends = {}

    # Iterate over the list of friend pairs
    for pair in friend_pairs:
        # Add the friends to the dictionary
        friends[pair[0]] = friends.get(pair[0], []) + [pair[1]]
        friends[pair[1]] = friends.get(pair[1], []) + [pair[0]]

    # Initialize a list to store the predicted friends of each user
    predicted_friends = []

    # Iterate over the dictionary of friends
    for user, friends in friends.items():
        # Get the predicted friends of the current user
        predicted_friends.append((user, get_predicted_friends(user, friends, k)))

    # Sort the predicted friends by their IDs in ascending order
    predicted_friends.sort(key=lambda x: x[0])

    # Return the predicted friends of each user
    return predicted_friends

def get_predicted_friends(user, friends, k):
    # Initialize a set to store the predicted friends of the current user
    predicted_friends = set()

    # Iterate over the friends of the current user
    for friend in friends:
        # Get the friends of the current friend
        friend_friends = friends.get(friend, [])

        # Add the current friend to the predicted friends if they have at least k% common friends with the current user
        if len(set(friend_friends).intersection(friends)) >= k:
            predicted_friends.add(friend)

    # Return the predicted friends of the current user
    return predicted_friends

if __name__ == '__main__':
    m, k = map(int, input().split())
    friend_pairs = []
    for _ in range(m):
        a, b = map(int, input().split())
        friend_pairs.append((a, b))
    predicted_friends = get_friends(m, k, friend_pairs)
    for user, friends in predicted_friends:
        print(f"{user}: {len(friends)} {' '.join(map(str, friends))}")

