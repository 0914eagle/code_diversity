
def get_friends(m, k, friendships):
    # Initialize a dictionary to store the friends of each user
    friends = {}

    # Iterate over the list of friendships
    for i in range(m):
        # Get the IDs of the two users in the current friendship
        user1, user2 = friendships[i]

        # If the user is not already in the dictionary, add them with an empty list of friends
        if user1 not in friends:
            friends[user1] = []
        if user2 not in friends:
            friends[user2] = []

        # Add the other user as a friend to both users
        friends[user1].append(user2)
        friends[user2].append(user1)

    # Initialize a dictionary to store the predicted friends of each user
    predicted_friends = {}

    # Iterate over the dictionary of friends
    for user, friend_list in friends.items():
        # Initialize a set to store the predicted friends of the current user
        predicted_friends[user] = set()

        # Iterate over the list of friends of the current user
        for friend in friend_list:
            # If the friend has at least k% of the current user's friends as friends, add them to the set of predicted friends
            if len(set(friends[friend]) & set(friends[user])) >= k:
                predicted_friends[user].add(friend)

    # Return the dictionary of predicted friends
    return predicted_friends

def print_predicted_friends(predicted_friends):
    # Sort the dictionary by user ID in ascending order
    sorted_friends = sorted(predicted_friends.items(), key=lambda x: x[0])

    # Iterate over the sorted dictionary
    for user, friend_set in sorted_friends:
        # Print the user ID and the number of predicted friends
        print(f"{user}: {len(friend_set)}")

        # Print the IDs of the predicted friends in ascending order
        for friend in sorted(friend_set):
            print(f"{friend}")

if __name__ == '__main__':
    m, k = map(int, input().split())
    friendships = []
    for _ in range(m):
        user1, user2 = map(int, input().split())
        friendships.append((user1, user2))
    predicted_friends = get_friends(m, k, friendships)
    print_predicted_friends(predicted_friends)

