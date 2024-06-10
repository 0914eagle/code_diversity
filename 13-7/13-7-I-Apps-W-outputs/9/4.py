
def get_friend_pairs(m, k, friend_pairs):
    # Initialize an empty dictionary to store the friend pairs
    friend_dict = {}

    # Iterate over the list of friend pairs
    for pair in friend_pairs:
        # Add the pair to the dictionary
        friend_dict[pair[0]] = friend_dict.get(pair[0], []) + [pair[1]]
        friend_dict[pair[1]] = friend_dict.get(pair[1], []) + [pair[0]]

    # Initialize an empty list to store the predicted friends
    predicted_friends = []

    # Iterate over the dictionary
    for user in friend_dict:
        # Get the list of friends for the current user
        friends = friend_dict[user]

        # Initialize a set to store the predicted friends
        predicted_friends_set = set()

        # Iterate over the list of friends
        for friend in friends:
            # Get the list of friends for the current friend
            friend_friends = friend_dict[friend]

            # Iterate over the list of friend friends
            for friend_friend in friend_friends:
                # Check if the friend friend is not already in the predicted friends set
                if friend_friend not in predicted_friends_set:
                    # Add the friend friend to the predicted friends set
                    predicted_friends_set.add(friend_friend)

        # Convert the predicted friends set to a list and sort it
        predicted_friends.append(sorted(list(predicted_friends_set)))

    return predicted_friends

def main():
    m, k = map(int, input().split())
    friend_pairs = []
    for _ in range(m):
        pair = list(map(int, input().split()))
        friend_pairs.append(pair)
    predicted_friends = get_friend_pairs(m, k, friend_pairs)
    for i, friends in enumerate(predicted_friends):
        print(f"{i+1}: {len(friends)} {', '.join(map(str, friends))}")

if __name__ == '__main__':
    main()

