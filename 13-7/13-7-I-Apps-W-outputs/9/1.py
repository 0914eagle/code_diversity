
def get_friends(m, k, friends):
    # Initialize a dictionary to store the friends of each user
    friend_dict = {}

    # Iterate over the list of friends
    for i in range(m):
        # Get the current friend pair
        friend_pair = friends[i]

        # Add the current friend pair to the dictionary
        if friend_pair[0] not in friend_dict:
            friend_dict[friend_pair[0]] = [friend_pair[1]]
        else:
            friend_dict[friend_pair[0]].append(friend_pair[1])

        if friend_pair[1] not in friend_dict:
            friend_dict[friend_pair[1]] = [friend_pair[0]]
        else:
            friend_dict[friend_pair[1]].append(friend_pair[0])

    # Iterate over the dictionary and find the predicted friends for each user
    predicted_friends = {}
    for user, friends in friend_dict.items():
        # Get the predicted friends for the current user
        predicted_friends[user] = get_predicted_friends(user, friends, k)

    return predicted_friends

def get_predicted_friends(user, friends, k):
    # Initialize a set to store the predicted friends
    predicted_friends = set()

    # Iterate over the friends of the current user
    for friend in friends:
        # Check if the friend is also a friend of the current user
        if friend in friends:
            # Add the friend to the set of predicted friends
            predicted_friends.add(friend)

    # Return the set of predicted friends
    return predicted_friends

def main():
    # Read the input data
    m, k = map(int, input().split())
    friends = []
    for i in range(m):
        friends.append(list(map(int, input().split())))

    # Get the predicted friends for each user
    predicted_friends = get_friends(m, k, friends)

    # Print the results
    for user, friends in predicted_friends.items():
        print(f"{user}: {len(friends)} {*friends,}")

if __name__ == '__main__':
    main()

