
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
    
    # Iterate over the users
    for user in range(1, m+1):
        # Get the list of friends of the current user
        friend_list = friends.get(user, [])
        
        # Initialize a set to store the predicted friends of the current user
        predicted_friends_set = set()
        
        # Iterate over the friends of the current user
        for friend in friend_list:
            # Get the list of friends of the current friend
            friend_list_2 = friends.get(friend, [])
            
            # Iterate over the friends of the current friend
            for friend_2 in friend_list_2:
                # If the friend is not the current user and is not already in the predicted friends set, add it to the set
                if friend_2 != user and friend_2 not in predicted_friends_set:
                    predicted_friends_set.add(friend_2)
        
        # Convert the set to a list and sort it
        predicted_friends.append(sorted(list(predicted_friends_set)))
    
    return predicted_friends

def main():
    m, k = map(int, input().split())
    friend_pairs = []
    for _ in range(m):
        friend_pairs.append(tuple(map(int, input().split())))
    predicted_friends = get_friends(m, k, friend_pairs)
    for user, friends in enumerate(predicted_friends, 1):
        print(f"{user}: {len(friends)} {' '.join(map(str, friends))}")

if __name__ == '__main__':
    main()

