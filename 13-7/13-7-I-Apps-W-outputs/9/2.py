
def get_friends(m, k, friend_pairs):
    # Initialize an empty dictionary to store the friends of each user
    friends = {}

    # Iterate over the list of friend pairs
    for pair in friend_pairs:
        # Extract the two users in the pair
        user1, user2 = pair

        # If the first user is not in the dictionary, add them with an empty set of friends
        if user1 not in friends:
            friends[user1] = set()

        # If the second user is not in the dictionary, add them with an empty set of friends
        if user2 not in friends:
            friends[user2] = set()

        # Add the second user to the set of friends of the first user
        friends[user1].add(user2)

        # Add the first user to the set of friends of the second user
        friends[user2].add(user1)

    # Iterate over the dictionary of friends
    for user, friend_set in friends.items():
        # If the user has at least k friends, add them to the output
        if len(friend_set) >= k:
            yield user, friend_set

def get_predictive_friends(m, k, friend_pairs):
    # Initialize an empty dictionary to store the predictive friends of each user
    predictive_friends = {}

    # Iterate over the list of friend pairs
    for pair in friend_pairs:
        # Extract the two users in the pair
        user1, user2 = pair

        # If the first user is not in the dictionary, add them with an empty set of predictive friends
        if user1 not in predictive_friends:
            predictive_friends[user1] = set()

        # If the second user is not in the dictionary, add them with an empty set of predictive friends
        if user2 not in predictive_friends:
            predictive_friends[user2] = set()

        # Add the second user to the set of predictive friends of the first user
        predictive_friends[user1].add(user2)

        # Add the first user to the set of predictive friends of the second user
        predictive_friends[user2].add(user1)

    # Iterate over the dictionary of predictive friends
    for user, friend_set in predictive_friends.items():
        # If the user has at least k friends, add them to the output
        if len(friend_set) >= k:
            yield user, friend_set

def main():
    m, k = map(int, input().split())
    friend_pairs = []
    for _ in range(m):
        user1, user2 = map(int, input().split())
        friend_pairs.append((user1, user2))

    friends = list(get_friends(m, k, friend_pairs))
    predictive_friends = list(get_predictive_friends(m, k, friend_pairs))

    # Print the results
    for user, friend_set in friends:
        print(f"{user}: {len(friend_set)} {' '.join(map(str, friend_set))}")
    for user, friend_set in predictive_friends:
        print(f"{user}: {len(friend_set)} {' '.join(map(str, friend_set))}")

if __name__ == '__main__':
    main()

