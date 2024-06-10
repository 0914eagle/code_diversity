
def get_friend_pairs(m, k, friend_pairs):
    # Initialize a dictionary to store the friend pairs
    friends = {}
    
    # Iterate over the list of friend pairs
    for i in range(m):
        # Extract the ids of the two friends from the pair
        id1, id2 = friend_pairs[i]
        
        # Add the friend pair to the dictionary
        if id1 not in friends:
            friends[id1] = [id2]
        else:
            friends[id1].append(id2)
        if id2 not in friends:
            friends[id2] = [id1]
        else:
            friends[id2].append(id1)
    
    # Iterate over the dictionary of friends
    for id, friend_list in friends.items():
        # Sort the list of friends for each user
        friend_list.sort()
        # Print the user id and the list of friends
        print(f"{id}: {len(friend_list)}", *friend_list)

def get_predicted_friends(m, k, friend_pairs):
    # Initialize a dictionary to store the predicted friends for each user
    predicted_friends = {}
    
    # Iterate over the list of friend pairs
    for i in range(m):
        # Extract the ids of the two friends from the pair
        id1, id2 = friend_pairs[i]
        
        # Add the friend pair to the dictionary
        if id1 not in predicted_friends:
            predicted_friends[id1] = [id2]
        else:
            predicted_friends[id1].append(id2)
        if id2 not in predicted_friends:
            predicted_friends[id2] = [id1]
        else:
            predicted_friends[id2].append(id1)
    
    # Iterate over the dictionary of predicted friends
    for id, friend_list in predicted_friends.items():
        # Sort the list of friends for each user
        friend_list.sort()
        # Print the user id and the list of predicted friends
        print(f"{id}: {len(friend_list)}", *friend_list)

if __name__ == '__main__':
    m, k = map(int, input().split())
    friend_pairs = []
    for _ in range(m):
        friend_pairs.append(tuple(map(int, input().split())))
    
    get_friend_pairs(m, k, friend_pairs)
    get_predicted_friends(m, k, friend_pairs)

