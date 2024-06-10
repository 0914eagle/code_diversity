
def get_friends(m, k, friends):
    # Initialize a dictionary to store the friends of each user
    friends_dict = {}
    
    # Iterate over the list of friends
    for i in range(m):
        # Get the current friend pair
        friend_pair = friends[i]
        
        # Add the first friend to the dictionary if it doesn't exist
        if friend_pair[0] not in friends_dict:
            friends_dict[friend_pair[0]] = []
        
        # Add the second friend to the dictionary if it doesn't exist
        if friend_pair[1] not in friends_dict:
            friends_dict[friend_pair[1]] = []
        
        # Add the first friend to the list of friends of the second friend
        friends_dict[friend_pair[1]].append(friend_pair[0])
        
        # Add the second friend to the list of friends of the first friend
        friends_dict[friend_pair[0]].append(friend_pair[1])
    
    # Initialize a list to store the predicted friends for each user
    predicted_friends = []
    
    # Iterate over the dictionary of friends
    for user, friends in friends_dict.items():
        # Get the predicted friends for the current user
        predicted_friends.append(get_predicted_friends(user, friends, k))
    
    # Return the predicted friends for each user
    return predicted_friends

def get_predicted_friends(user, friends, k):
    # Initialize a set to store the predicted friends
    predicted_friends = set()
    
    # Iterate over the list of friends
    for friend in friends:
        # If the friend is not the current user
        if friend != user:
            # Add the friend to the set of predicted friends
            predicted_friends.add(friend)
    
    # Return the predicted friends
    return predicted_friends

def main():
    # Read the input data
    m, k = map(int, input().split())
    friends = []
    for i in range(m):
        friend_pair = list(map(int, input().split()))
        friends.append(friend_pair)
    
    # Get the predicted friends for each user
    predicted_friends = get_friends(m, k, friends)
    
    # Print the predicted friends for each user
    for i, user in enumerate(predicted_friends):
        print(f"{i+1}: {len(user)} {' '.join(map(str, user))}")

if __name__ == '__main__':
    main()

